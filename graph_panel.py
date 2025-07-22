# graph_panel.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import deque

class TrafficGraph(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(200)

        self.layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(6, 2.5)))
        self.ax = self.canvas.figure.subplots()
        self.layout.addWidget(self.canvas)

        self.inbound_data = deque([0] * 60, maxlen=60)
        self.outbound_data = deque([0] * 60, maxlen=60)
        self.x_data = list(range(-59, 1))

        self.inbound_plot, = self.ax.plot(self.x_data, list(self.inbound_data), label="📥 Gelen", color="green")
        self.outbound_plot, = self.ax.plot(self.x_data, list(self.outbound_data), label="📤 Giden", color="blue")

        self.ax.set_ylim(0, 1500)
        self.ax.set_xlim(-59, 0)
        self.ax.legend()
        self.ax.set_title("📊 Canlı Trafik (B/s)")

        self.ax.set_xlabel("Saniye")
        self.ax.set_ylabel("Bayt")

    def update_graph(self, inbound_bytes, outbound_bytes):
        self.inbound_data.append(inbound_bytes)
        self.outbound_data.append(outbound_bytes)
        self.inbound_plot.set_ydata(self.inbound_data)
        self.outbound_plot.set_ydata(self.outbound_data)
        self.canvas.draw()
