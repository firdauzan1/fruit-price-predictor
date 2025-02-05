from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path

app = FastAPI(
    title="Fruit Price Predictor",
    description="API untuk memprediksi harga buah menggunakan machine learning",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain Render Anda nanti
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup paths
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
MODEL_DIR = BASE_DIR / "model"

# Mount static files dan templates
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Load model - with error handling
try:
    model = joblib.load(MODEL_DIR / 'fruit_price_predictor.joblib')
    scaler = joblib.load(MODEL_DIR / 'scaler.joblib')
    le_form = joblib.load(MODEL_DIR / 'form_encoder.joblib')
except Exception as e:
    print(f"Error loading models: {str(e)}")
    raise

class PredictionInput(BaseModel):
    form_type: str
    yield_val: float
    cup_price: float

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "fruit_forms": le_form.classes_.tolist()}
    )

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Input validation
        if input_data.yield_val <= 0 or input_data.cup_price <= 0:
            return {
                "success": False,
                "error": "Yield dan Cup Price harus lebih besar dari 0"
            }
            
        # Form validation
        if input_data.form_type not in le_form.classes_:
            return {
                "success": False,
                "error": "Bentuk buah tidak valid"
            }
            
        # Encode form type
        form_encoded = le_form.transform([input_data.form_type])[0]
        predictions = []
        
        # Bootstrap predictions
        for _ in range(100):
            yield_noise = input_data.yield_val * (1 + np.random.normal(0, 0.1))
            cup_price_noise = input_data.cup_price * (1 + np.random.normal(0, 0.1))
            
            input_df = pd.DataFrame(
                [[form_encoded, yield_noise, cup_price_noise]],
                columns=['Form_encoded', 'Yield', 'CupEquivalentPrice']
            )
            
            input_scaled = pd.DataFrame(
                scaler.transform(input_df),
                columns=['Form_encoded', 'Yield', 'CupEquivalentPrice']
            )
            
            pred = model.predict(input_scaled)[0]
            predictions.append(pred)
        
        # Calculate statistics
        predictions = np.array(predictions)
        mean_pred = float(np.mean(predictions))
        ci_lower = float(np.percentile(predictions, 2.5))
        ci_upper = float(np.percentile(predictions, 97.5))
        
        return {
            "success": True,
            "prediction": round(mean_pred, 2),
            "ci_lower": round(ci_lower, 2),
            "ci_upper": round(ci_upper, 2)
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error dalam kalkulasi: {str(e)}"
        }

# Optional: health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}