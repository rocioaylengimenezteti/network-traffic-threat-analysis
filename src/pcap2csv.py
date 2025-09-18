import pyshark
import pandas as pd
import os

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
# Create the 'processed' folder if it doesn't exist
# Crear carpeta processed si no existe
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def pcap_to_csv(pcap_file):
    print(f"[INFO] Procesando {pcap_file}...")
    
    cap = pyshark.FileCapture(
        pcap_file,
        tshark_path=r"C:\Users\rocio\Desktop\Wireshark\tshark.exe"
    )

    data = []
    for pkt in cap:
     
        row = {
            "time": getattr(pkt, "sniff_time", ""),
            "src_ip": getattr(pkt.ip, "src", "") if hasattr(pkt, "ip") else "",
            "dst_ip": getattr(pkt.ip, "dst", "") if hasattr(pkt, "ip") else "",
            "src_port": getattr(pkt[pkt.highest_layer.lower()], "srcport", "") if hasattr(pkt, pkt.highest_layer.lower()) else "",
            "dst_port": getattr(pkt[pkt.highest_layer.lower()], "dstport", "") if hasattr(pkt, pkt.highest_layer.lower()) else "",
            "protocol": pkt.highest_layer,
            "length": pkt.length
        }

        data.append(row)  

    df = pd.DataFrame(data)
    csv_file = os.path.join(PROCESSED_DATA_DIR, os.path.basename(pcap_file).replace(".pcap", ".csv"))
    df.to_csv(csv_file, index=False)
    print(f"[INFO] Guardado CSV en {csv_file}")

def main():
    for filename in os.listdir(RAW_DATA_DIR):
        if filename.endswith(".pcap"):
            pcap_to_csv(os.path.join(RAW_DATA_DIR, filename))

if __name__ == "__main__":
    main()
