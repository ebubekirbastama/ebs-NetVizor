# main.py
import sys
from PyQt5.QtWidgets import QApplication
from threading import Thread
from sniffer import start_sniffing
from ui_main import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    def run_sniffer():
        start_sniffing(window.add_packet)

    sniff_thread = Thread(target=run_sniffer, daemon=True)
    sniff_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
