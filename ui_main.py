# ui_main.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QComboBox, QLineEdit, QPushButton, QTabWidget
)
from PyQt5.QtCore import QTimer
from graph_panel import TrafficGraph
from app_traffic import get_active_connections
from geoip import get_ip_location

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌐 NetVizor - Ağ Trafiği Analiz Aracı")
        self.resize(1000, 700)

        self.layout = QVBoxLayout(self)

        # Filtre alanı
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("🔎 Protokol:"))
        self.protocol_filter = QComboBox()
        self.protocol_filter.addItems(["Hepsi", "TCP", "UDP", "ICMP"])
        filter_layout.addWidget(self.protocol_filter)

        filter_layout.addWidget(QLabel("🔢 Port:"))
        self.port_filter = QLineEdit()
        self.port_filter.setPlaceholderText("Örn: 80, 443 veya boş")
        filter_layout.addWidget(self.port_filter)

        self.filter_btn = QPushButton("Filtreyi Uygula")
        filter_layout.addWidget(self.filter_btn)
        self.layout.addLayout(filter_layout)

        # Sekmeler
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Ağ Trafiği sekmesi
        self.tab_traffic = QWidget()
        self.tabs.addTab(self.tab_traffic, "📡 Ağ Trafiği")

        # Uygulama Trafiği sekmesi
        self.tab_apps = QWidget()
        self.tabs.addTab(self.tab_apps, "📊 Uygulama Trafiği")

        # Ağ Trafiği sekmesi düzeni
        traffic_layout = QVBoxLayout(self.tab_traffic)
        self.label = QLabel("🚦 Trafik Takibi Başlatıldı...", self)
        traffic_layout.addWidget(self.label)

        self.traffic_graph = TrafficGraph(self)
        traffic_layout.addWidget(self.traffic_graph)

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "➡️ Yön", "🔗 Protokol", "📍 Kaynak IP", "📍 Hedef IP",
            "🔢 Portlar", "🌍 Konum"
        ])
        traffic_layout.addWidget(self.table)

        # Uygulama Trafiği sekmesi düzeni
        apps_layout = QVBoxLayout(self.tab_apps)
        self.app_table = QTableWidget(0, 5)
        self.app_table.setHorizontalHeaderLabels(["PID", "Uygulama", "Yerel Adres", "Uzak Adres", "Durum"])
        apps_layout.addWidget(self.app_table)

        # Timerlar
        self.current_in = 0
        self.current_out = 0

        self.filter_btn.clicked.connect(self.apply_filter)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graph_data)
        self.timer.start(1000)

        self.app_timer = QTimer()
        self.app_timer.timeout.connect(self.update_app_traffic)
        self.app_timer.start(5000)

        # Aktif filtreler
        self.active_protocol = None
        self.active_port = None

    def apply_filter(self):
        proto = self.protocol_filter.currentText()
        self.active_protocol = proto if proto != "Hepsi" else None

        port_text = self.port_filter.text().strip()
        if port_text.isdigit():
            self.active_port = int(port_text)
        else:
            self.active_port = None

        self.table.setRowCount(0)
        self.label.setText(f"🚦 Filtre uygulandı: Protokol={self.active_protocol or 'Hepsi'}, Port={self.active_port or 'Hepsi'}")

    def add_packet(self, pkt):
        # Filtreleme
        if self.active_protocol and pkt["protocol"].upper() != self.active_protocol.upper():
            return
        if self.active_port:
            if pkt["src_port"] != self.active_port and pkt["dst_port"] != self.active_port:
                return

        # IP konumu al (yalnızca hedef IP için hız için)
        city, country, _ = get_ip_location(pkt["dst_ip"])
        location_str = f"{city}, {country}"

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(pkt["direction"]))
        self.table.setItem(row, 1, QTableWidgetItem(pkt["protocol"]))
        self.table.setItem(row, 2, QTableWidgetItem(pkt["src_ip"]))
        self.table.setItem(row, 3, QTableWidgetItem(pkt["dst_ip"]))
        self.table.setItem(row, 4, QTableWidgetItem(f"{pkt['src_port']} → {pkt['dst_port']}"))
        self.table.setItem(row, 5, QTableWidgetItem(location_str))

        length = pkt.get("length", 500)
        if pkt["direction"] == "inbound":
            self.current_in += length
        else:
            self.current_out += length

    def update_graph_data(self):
        self.traffic_graph.update_graph(self.current_in, self.current_out)
        self.current_in = 0
        self.current_out = 0

    def update_app_traffic(self):
        self.app_table.setRowCount(0)
        connections = get_active_connections()
        for conn in connections:
            row = self.app_table.rowCount()
            self.app_table.insertRow(row)
            self.app_table.setItem(row, 0, QTableWidgetItem(str(conn["pid"])))
            self.app_table.setItem(row, 1, QTableWidgetItem(conn["process_name"]))
            self.app_table.setItem(row, 2, QTableWidgetItem(conn["laddr"]))
            self.app_table.setItem(row, 3, QTableWidgetItem(conn["raddr"]))
            self.app_table.setItem(row, 4, QTableWidgetItem(conn["status"]))
