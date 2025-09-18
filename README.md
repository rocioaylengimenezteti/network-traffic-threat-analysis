1. Project Description

    This project allows analyzing network traffic captured in .pcap files, identifying suspicious or potentially malicious patterns, and displaying an advanced professional dashboard with alerts and security recommendations.

    Main Features:

    Filters only critical traffic: packets without IP, large packets, unusual protocols (TLS/HTTP), suspicious ICMP.

    Detailed explanations of why each packet is suspicious.

    Professional action recommendations.

    Responsive dashboard with charts of suspicious traffic patterns (Chart.js).

    Prepared for presenting results to cybersecurity companies.

2. Requirements

        Python 3.12+

        Wireshark (with tshark.exe available)

    Python Libraries:

        pyshark

        pandas

    Quick installation on Windows:

# Create virtual environment
    py -3.12 -m venv venv
    .\venv\Scripts\Activate.ps1

# Install libraries
    pip install pyshark pandas

    Make sure Wireshark is installed and tshark.exe is accessible, for example at:

        C:\Users\<username>\Desktop\Wireshark\tshark.exe

3. Project Structure
ids-project/
│
├─ data/
│  ├─ raw/          # Folder to place original .pcap files
│  └─ processed/    # Folder where generated CSVs will be saved
│
├─ notebooks/       # Optional, for analysis or experiments
├─ models/          # Optional, for ML models
│
├─ src/
│  └─ pcap2csv.py   # Script to convert .pcap to CSV
│
├─ suspicious_analysis.html  # Advanced dashboard for traffic analysis
└─ README.md

4. How to Generate a CSV from a PCAP File

    Place your .pcap file in the data/raw/ folder.
    Example:

     data/raw/xplit.pcap

    Run the Python script pcap2csv.py from the project root:

# Activate virtual environment
    .\venv\Scripts\Activate.ps1

# Run conversion
    python src\pcap2csv.py


    The script will process all .pcap files in data/raw/ and generate .csv files in data/processed/.
    Example:

        data/processed/xplit.csv


    Each CSV will have columns:

        time – Packet capture timestamp

        src_ip / dst_ip – Source and destination IPs (missing IP is suspicious)

        src_port / dst_port – Source and destination ports

        protocol – Protocol type (TCP, UDP, ICMP, TLS, HTTP, etc.)

        length – Packet size in bytes

5. How to Use the HTML Dashboard

    Open suspicious_analysis.html in any modern browser (Chrome, Edge, Firefox).

    Select the generated CSV file (e.g., data/processed/xplit.csv).

    The dashboard will display:

    Critical alerts table:
        Only the most suspicious packets.

        Professional explanations of why they are critical.

        Immediate action recommendations.

        Chart of packet bursts per IP (to detect active scanning or unusual traffic).

    Alert Types:

        Level	Meaning	Recommended Action
        High	Critical packet: missing IP, very large → possible exfiltration or spoofing	Investigate source/destination IP, block if external, alert SOC
        Medium	Unusual TLS/HTTP, ICMP → possible reconnaissance or data exfiltration	Review open ports, analyze certificates, audit services
6. What to Look For and Why It’s Suspicious

    Missing source or destination IP → Manipulated traffic or spoofing

    Large packets (>1000 bytes) → Possible data exfiltration

    Unusual TLS/HTTP → Data exfiltration or encrypted tunnels

    ICMP → Network scanning or reconnaissance

    Bursts of packets from the same IP or port → Active network scanning

7. Professional Recommendations

    Analyze high-alert packets first; ignore normal browsing traffic.

    Block suspicious external IP addresses.

    Monitor unusual ports.

    Review TLS certificates and anomalous HTTP patterns.

    Keep detailed logs of all analyses for auditing purposes.

8. Final Considerations

    This project is designed for professional cybersecurity use and is ready to show clear, precise results with advanced technical explanations to any SOC team or leading security company.


-------------------------------------------------------------------------------------------------------------------------
1. Descripción del proyecto

    Este proyecto permite analizar tráfico de red capturado en archivos .pcap, identificar patrones sospechosos o potencialmente maliciosos, y mostrar un dashboard avanzado y profesional con alertas y recomendaciones de seguridad.

    Características principales:

    Filtra solo tráfico crítico: paquetes sin IP, de gran tamaño, protocolos inusuales (TLS/HTTP), ICMP sospechoso.

    Explicaciones detalladas de por qué cada paquete es sospechoso.

    Recomendaciones de acción profesional.

    Dashboard responsive con gráficos de patrones de tráfico sospechoso (Chart.js).

    Preparado para presentar resultados a empresas de ciberseguridad.

2. Requisitos

        Python 3.12+

        Wireshark (con tshark.exe disponible)

    Librerías Python:

        pyshark

        pandas

    Instalación rápida en Windows:

# Crear entorno virtual
    py -3.12 -m venv venv
    .\venv\Scripts\Activate.ps1

# Instalar librerías
    pip install pyshark pandas


    Asegúrate de tener Wireshark instalado y tshark.exe accesible, por ejemplo en:

            C:\Users\<usuario>\Desktop\Wireshark\tshark.exe

3. Estructura del proyecto
ids-project/
│
├─ data/
│  ├─ raw/          # Carpeta donde colocar los archivos .pcap originales
│  └─ processed/    # Carpeta donde se guardarán los CSV generados
│
├─ notebooks/         ← opcional, para análisis o experimentos
├─ models/            ← opcional, para modelos ML
|
├─ src/
│  └─ pcap2csv.py   # Script para convertir .pcap a CSV
│
├─ analisis_sospechoso.html  # Dashboard avanzado para análisis de tráfico
└─ README.md

4. Cómo generar un CSV desde un archivo PCAP

    Coloca tu archivo .pcap en la carpeta data/raw/.
    Ejemplo:

        data/raw/xplit.pcap


    Ejecuta el script Python pcap2csv.py desde la raíz del proyecto:

# Activar entorno virtual
    .\venv\Scripts\Activate.ps1

# Ejecutar conversión
         python src\pcap2csv.py


    El script procesará todos los archivos .pcap de data/raw/ y generará archivos .csv en data/processed/.
    Ejemplo:

        data/processed/xplit.csv


    Cada CSV tendrá columnas:

        time	src_ip	dst_ip	src_port	dst_port	protocol	length

        time: Hora de captura del paquete.

        src_ip / dst_ip: IP de origen y destino (si falta, es sospechoso).

        src_port / dst_port: Puertos de origen/destino.

        protocol: Tipo de protocolo (TCP, UDP, ICMP, TLS, HTTP, etc.)

        length: Tamaño del paquete en bytes.

5. Cómo usar el dashboard HTML

    Abre el archivo analisis_sospechoso.html en cualquier navegador moderno (Chrome, Edge, Firefox).

    Selecciona el archivo CSV generado (data/processed/xplit.csv).

    El dashboard mostrará:

    Tabla de alertas críticas:

    Solo los paquetes más sospechosos.

    Explicaciones profesionales del por qué son críticos.

    Recomendaciones de acción inmediata.

    Gráfica de ráfagas de paquetes por IP (detectar escaneo activo o tráfico inusual).

    Tipos de alerta:
    Nivel	Qué significa	Qué hacer
    Alto	Paquete crítico: sin IP, muy grande → posible exfiltración o spoofing	Investigar la IP origen/destino, bloquear si es externo, alertar SOC
    Medio	Tráfico TLS/HTTP inusual, ICMP → posible reconocimiento o fuga de datos	Revisar puertos abiertos, analizar certificados, auditar servicios
6. Qué buscar y por qué es sospechoso

    Falta de IP de origen o destino → tráfico manipulado o spoofing.

    Paquetes grandes (>1000 bytes) → posible exfiltración de información.

    TLS/HTTP raro → exfiltración de datos o túneles cifrados.

    ICMP → escaneo de red o reconocimiento.

    Ráfagas de paquetes de la misma IP o puerto → escaneo activo de la red.

7. Recomendaciones profesionales

    Analiza primero los paquetes de alerta alta, ignora el tráfico normal de navegación.

    Bloquea direcciones IP externas sospechosas.

    Monitorea puertos inusuales.

    Revisa certificados TLS y patrones HTTP anómalos.

    Mantén registros de todo análisis para auditoría.

8. Consideraciones finales

    Este proyecto está diseñado para uso profesional en ciberseguridad y está preparado para mostrar resultados claros, precisos y con explicaciones técnicas avanzadas a cualquier equipo SOC o empresa de seguridad líder.