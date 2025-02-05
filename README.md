# 🍎 Fruit Price Predictor

Aplikasi web modern untuk memprediksi harga buah menggunakan Machine Learning dengan fitur UI yang interaktif.

## ✨ Fitur

- 🎯 Prediksi harga buah dengan akurasi tinggi
- 📊 Interval kepercayaan 95% untuk setiap prediksi
- 🌓 Mode Gelap/Terang
- 💫 Animasi dan transisi halus
- 📱 Responsive design untuk semua ukuran layar
- 🎨 UI Modern dengan efek glassmorphism

## 🏗️ Teknologi yang Digunakan

- **Backend:**
  - FastAPI (Python web framework)
  - Scikit-learn (Machine Learning)
  - Pandas & NumPy (Data processing)
  - Joblib (Model serialization)

- **Frontend:**
  - HTML5 & CSS3
  - Bootstrap 5.3
  - Font Awesome icons
  - JavaScript (Vanilla)

## 📁 Struktur Folder

project/ ├── app.py # FastAPI application ├── templates/
│ └── index.html # HTML template dengan dark/light mode ├── static/ # Static files folder └── model/ # Model files ├── fruit_price_predictor.joblib ├── scaler.joblib └── form_encoder.joblib

## 🚀 Cara Menjalankan Aplikasi

1. Install dependencies:
```bash
pip install -r requirements.txt

💡 Cara Penggunaan

Pilih bentuk buah dari dropdown menu
Masukkan nilai yield (minimal 0.1)
Masukkan cup equivalent price (minimal 0.1)
Klik tombol "Prediksi Harga"
Lihat hasil prediksi dan interval kepercayaan

🎨 Fitur UI

Dark/Light Mode: Toggle di pojok kanan atas untuk mengubah tema
Animasi: Fade-in saat halaman dimuat dan hover effects
Glassmorphism: Efek transparansi modern pada cards
Loading State: Spinner animasi saat memproses prediksi
Responsive: Tampilan optimal di desktop dan mobile

🤝 Kontribusi

Kontribusi selalu diterima! Berikut langkah-langkahnya:

Fork repository ini
Buat branch baru (git checkout -b fitur-baru)
Commit perubahan (git commit -m 'Menambah fitur baru')
Push ke branch (git push origin fitur-baru)
Buat Pull Request

📝 Catatan
Pastikan semua file model (.joblib) tersedia di folder model/
Aplikasi membutuhkan koneksi internet untuk memuat CDN (Bootstrap, Font Awesome)
Minimal Python 3.7 atau lebih tinggi