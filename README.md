# Prediksi Harga Saham

Proyek ini adalah aplikasi sederhana untuk memprediksi harga saham menggunakan Jaringan Saraf Tiruan (JST). Aplikasi ini mengambil data historis harga saham dan memberikan prediksi harga di masa depan berdasarkan model yang dilatih.

## Struktur Proyek

prediksi_harga_saham/ │ ├── data/ │ └── dataset.csv # (Opsional: Anda bisa menambahkan dataset di sini) │ ├── src/ │ ├── main.py # File utama untuk menjalankan aplikasi │ ├── model.py # File untuk mendefinisikan model JST │ └── fuzzy.py # File untuk mendefinisikan logika fuzzy (jika diperlukan) │ ├── requirements.txt # Daftar dependensi └── README.md # Deskripsi proyek

## Cara Menggunakan

1. Clone repositori ini.
2. Install dependensi dengan menjalankan `pip install -r requirements.txt`.
3. Siapkan dataset harga saham dalam format CSV di folder `data/`.
4. Jalankan aplikasi dengan menjalankan `python src/main.py`.

## Dataset

Anda dapat menggunakan dataset harga saham dari sumber seperti Yahoo Finance atau Alpha Vantage.