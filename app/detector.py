from sklearn.ensemble import IsolationForest
import joblib

def train_model(df):
    features = df[["len", "proto"]]
    model = IsolationForest(contamination=0.01)
    model.fit(features)
    joblib.dump(model, "model/anomaly_model.pkl")

def detect_anomalies(df):
    model = joblib.load("model/anomaly_model.pkl")
    features = df[["len", "proto"]]
    df["anomaly"] = model.predict(features)  # -1 = anomaly
    return df
