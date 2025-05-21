def generate_alerts(df):
    anomalies = df[df["anomaly"] == -1]
    alerts = []

    for _, row in anomalies.iterrows():
        alerts.append({
            "timestamp": row["time"],
            "source": row["src"],
            "destination": row["dst"],
            "description": "Anomalous packet detected"
        })

    return alerts
