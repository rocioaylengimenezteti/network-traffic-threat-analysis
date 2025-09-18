from scapy.all import sniff, wrpcap
from datetime import datetime

def capture_packets(interface, duration):
    """
    Captura paquetes de red durante `duration` segundos
    y los guarda en data/raw con un nombre basado en la fecha.
    """
    filename = f"data/raw/capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap"
    print(f"[INFO] Capturando tráfico en {interface} durante {duration} segundos...")
    packets = sniff(iface=interface, timeout=duration)
    wrpcap(filename, packets)
    print(f"[INFO] Captura guardada en {filename}")

if __name__ == "__main__":
    # Change 'Ethernet' to your network interface (Wi-Fi, Ethernet)
    # Cambia 'Ethernet' por tu interfaz de red (Wi-Fi, Ethernet)
    capture_packets(interface="Wi-Fi", duration=15)

