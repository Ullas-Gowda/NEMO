from scapy.all import rdpcap
import pandas as pd

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    data = []

    for pkt in packets:
        if pkt.haslayer("IP"):
            data.append({
                "src": pkt["IP"].src,
                "dst": pkt["IP"].dst,
                "proto": pkt["IP"].proto,
                "len": len(pkt),
                "time": pkt.time,
            })

    df = pd.DataFrame(data)
    return df
