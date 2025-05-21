# 🛡️ Network Anomaly Detection for Critical Infrastructure

A lightweight, real-time anomaly detection system designed for Industrial Control Systems (ICS) with low-bandwidth constraints. Built for **Hack to the Future 2.0**, this project monitors network traffic, learns normal behavior patterns, detects anomalies (both operational and malicious), and generates contextual alerts through a clean, minimal dashboard.

---

## 🚀 Features

- 📡 **Packet Capture & Parsing** using `scapy`
- 🧠 **Baseline Learning** with unsupervised ML (Isolation Forest)
- 🔍 **Anomaly Detection** in real-time or batch mode
- ⚠️ **Alert Generation** with contextual metadata
- 📊 **Web Dashboard** built with Flask for visualization
- 🪶 **Lightweight & Efficient**, designed to run in low-bandwidth ICS environments

---

## 🛠️ Tech Stack

| Layer | Tech |
|------|------|
| Language | Python |
| Packet Parsing | Scapy |
| ML/Anomaly Detection | scikit-learn (Isolation Forest) |
| Web Framework | Flask |
| Visualization | HTML / Bootstrap / Jinja2 |
| Optional DB | SQLite / InfluxDB (for future scalability) |

---

## 📂 Project Structure

```

network_anomaly_detector/
├── data/                    ← Sample .pcap traffic files
│   └── sample_traffic.pcap
├── model/                   ← Trained anomaly detection model
│   └── anomaly_model.pkl
├── app/                     ← Core modules
│   ├── baseline.py ← Parses network packets & extracts features
│   ├── detector.py ← Learns and detects anomalies
│   ├── alerting.py ← Generates contextual alerts
│   └── dashboard.py ← Flask dashboard for visualization
├── main.py                  ← Trains the baseline anomaly detection model
├── requirements.txt         ← Project dependencies
└── README.md                ← This file

````

---

## ⚙️ Installation

> Make sure you have Python 3.8+ installed.

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/network_anomaly_detector.git
cd network_anomaly_detector
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is empty, use:

```bash
pip install scapy pandas scikit-learn flask matplotlib joblib
```

---

## ▶️ How to Run

### 1. Train the Model on Normal Data

```bash
python main.py
```

### 2. Start the Dashboard

```bash
python app/dashboard.py
```

Then, visit [http://127.0.0.1:5000](http://127.0.0.1:5000/) in your browser.

---

## 🧪 Sample Output

Alerts look like this:

```
⏰ 1716328943.123 - 🧑‍💻 192.168.1.5 ➡ 10.0.0.7 - ⚠️ Anomalous packet detected
```

---

## 📦 Datasets

You can use real or simulated traffic:

-   [TON_IoT Datasets](https://research.unsw.edu.au/projects/toniot-datasets)

-   [CIC-IDS 2017](https://www.unb.ca/cic/datasets/ids-2017.html)

-   Custom .pcap files captured with Wireshark


---

## 🌟 Future Improvements

-   Live packet sniffing via `pyshark` or `libpcap`

-   Add auto-labeling with clustering (e.g., DBSCAN)

-   Edge compatibility (Raspberry Pi build)

-   Real-time email/SMS/Webhook alerts

-   Integration with InfluxDB + Grafana


---

## 👥 Authors




------

## 💡 Hackathon Impact

> This project aims to improve early detection of cyber-physical attacks in critical infrastructure with minimal resource consumption, enabling operational continuity and cyber resilience in smart cities and industries.

---

## 🧰 Commands Cheat Sheet

| Task | Command |
| --- | --- |
| Train Model | `python main.py` |
| Start Dashboard | `python app/dashboard.py` |
| Add pcap file | Put it in `data/` folder |
| Install packages | `pip install -r requirements.txt` |

---

## 🤝 Contributing

Want to improve or build on this? Fork it and go wild. PRs welcome!

---

