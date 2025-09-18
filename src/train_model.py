import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

PROCESSED_DATA_DIR = "data/processed"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    dfs = []
    for file in os.listdir(PROCESSED_DATA_DIR):
        if file.endswith(".csv"):
            dfs.append(pd.read_csv(os.path.join(PROCESSED_DATA_DIR, file)))
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        return df
    else:
        print("[WARN] No hay CSV para entrenar.")
        return None

def preprocess(df):
    # Convert protocols to numbers (simple encoding)
    # Convertir protocolos a números (simple encoding)
    df['protocol'] = df['protocol'].astype('category').cat.codes
    # Fill NaN values with 0
    # Rellenar NaN con 0
    df = df.fillna(0)
    # Select features and dummy label
    # Elegimos features y label dummy
    X = df[['protocol', 'length']]
    # For demo purposes, create a fictitious label (0 normal, 1 suspicious)
    # Para demo, creamos un label ficticio (0 normal, 1 sospechoso)
    import numpy as np
    y = np.random.randint(0,2,size=len(df))
    return X, y

def main():
    df = load_data()
    if df is None:
        return
    X, y = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    # Save model
    # Guardar modelo
    joblib.dump(model, os.path.join(MODEL_DIR, "ids_model.pkl"))
    print("[INFO] Modelo entrenado y guardado en models/ids_model.pkl")

if __name__ == "__main__":
    main()
