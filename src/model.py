import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers

def load_data(file_path):
    # Memuat dataset
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Menggunakan harga penutupan sebagai target
    data['Target'] = data['Close'].shift(-1)
    data = data.dropna()

    # Memisahkan fitur dan target
    X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = data['Target']

    # Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalisasi data
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

def build_model(input_shape):
    # Membangun model JST
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)  # Output harga
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model