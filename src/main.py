import pandas as pd
from model import load_data, preprocess_data, build_model
from fuzzy import fuzzy_adjustment

def main():
    # Memuat data
    data = load_data('data/dataset.csv')

    # Preprocessing data
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Membangun dan melatih model
    model = build_model(X_train.shape[1])
    model.fit(X_train, y_train, epochs=100, verbose=1)

    # Memprediksi harga saham
    predictions = model.predict(X_test)

    # Menampilkan hasil
    results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions.flatten()})
    print(results)

    # Misalkan kita mendapatkan kondisi pasar dari input pengguna
    market_condition = 60  # Contoh input kondisi pasar (0-100)

    # Menyesuaikan prediksi harga menggunakan logika fuzzy
    adjusted_price = fuzzy_adjustment(predictions.flatten()[0], market_condition)
    print(f"Harga yang Disesuaikan Berdasarkan Kondisi Pasar: {adjusted_price:.2f}")

if __name__ == "__main__":
    main()