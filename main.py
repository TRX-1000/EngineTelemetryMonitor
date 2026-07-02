# main.py
# Entry point for the Engine Telemetry Monitor application.

from engine_monitor import EngineMonitorApp
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EngineMonitorApp()
    w.show()
    sys.exit(app.exec_())