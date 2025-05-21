from flask import Flask, render_template_string
from app.baseline import extract_features
from app.detector import detect_anomalies
from app.alerting import generate_alerts

app = Flask(__name__)

@app.route("/")
def home():
    df = extract_features("data/sample_traffic.pcap")
    df = detect_anomalies(df)
    alerts = generate_alerts(df)

    html = """
    <h1>Network Anomaly Alerts</h1>
    <ul>
    {% for alert in alerts %}
      <li>{{ alert.timestamp }} - {{ alert.source }} ➡ {{ alert.destination }} - {{ alert.description }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)
