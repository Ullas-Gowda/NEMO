from app.baseline import extract_features
from app.detector import train_model

df = extract_features("data/sample_traffic.pcap")
train_model(df)
