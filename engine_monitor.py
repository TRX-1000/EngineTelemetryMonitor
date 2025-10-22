# main.py
# Run this to start the Engine Telemetry Monitor GUI.

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton, QSpinBox, QMessageBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QFont

from car_profiles import CAR_PROFILES
from telemetry_sim import generate_sensor_data
from fault_checker import check_faults
from engine_logger import log_entry
from system_logger import log_event

# Columns to display (order matters)
COLUMNS = [
    ("temperature", "Engine Temp (°C)"),
    ("oil_pressure", "Oil PSI"),
    ("rpm", "RPM"),
    ("coolant_level", "Coolant (%)"),
    ("battery_voltage", "Battery (V)"),
    ("fuel_efficiency", "Fuel eff (km/l)"),
    ("vibration_level", "Vibration"),
    ("emission_level", "Emissions"),
    ("engine_load", "Engine Load (%)"),
    ("intake_pressure", "Intake (kPa)"),
    ("throttle_position", "Throttle (%)"),
    ("air_fuel_ratio", "AFR")
]


class EngineMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Engine Telemetry Monitor")
        self.resize(1100, 640)

        self.profiles = CAR_PROFILES
        self.car_keys = list(self.profiles.keys())
        self.current_index = 0

        # UI layout
        main = QVBoxLayout()
        hdr = QHBoxLayout()
        ctrls = QHBoxLayout()

        # Header
        self.title = QLabel("✅ Engine Telemetry Monitor")
        self.title.setFont(QFont("Arial", 16, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        main.addWidget(self.title)

        # Car label
        self.car_label = QLabel("")
        self.car_label.setFont(QFont("Arial", 12))
        main.addWidget(self.car_label)

        # Table
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Parameter", "Value"])
        self.table.horizontalHeader().setStretchLastSection(True)
        main.addWidget(self.table)

        # Controls: prev/next, start/pause, interval
        self.prev_btn = QPushButton("⬅ Prev")
        self.next_btn = QPushButton("Next ➡")
        self.start_btn = QPushButton("▶ Start")
        self.pause_btn = QPushButton("⏸ Pause")
        self.pause_btn.setEnabled(False)

        self.interval_label = QLabel("Interval (s):")
        self.spin_interval = QSpinBox()
        self.spin_interval.setRange(1, 10)
        self.spin_interval.setValue(2)

        for w in (self.prev_btn, self.next_btn, self.start_btn, self.pause_btn, self.interval_label, self.spin_interval):
            ctrls.addWidget(w)
        ctrls.addStretch()
        main.addLayout(ctrls)

        # Connections
        self.prev_btn.clicked.connect(self.prev_car)
        self.next_btn.clicked.connect(self.next_car)
        self.start_btn.clicked.connect(self.start_monitoring)
        self.pause_btn.clicked.connect(self.pause_monitoring)
        self.spin_interval.valueChanged.connect(self.change_interval)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cycle)
        self.timer.setInterval(self.spin_interval.value() * 1000)

        # initial render
        self.setLayout(main)
        self.render_current_car_initial()

    def render_current_car_initial(self):
        key = self.car_keys[self.current_index]
        p = self.profiles[key]
        self.car_label.setText(f"{p['make']} {p['model']} — {key} ({p['year']})")
        # build rows equal to number of columns
        self.table.setRowCount(len(COLUMNS))
        for row, (param, title) in enumerate(COLUMNS):
            self.table.setItem(row, 0, QTableWidgetItem(title))
            self.table.setItem(row, 1, QTableWidgetItem("—"))

    def prev_car(self):
        self.current_index = (self.current_index - 1) % len(self.car_keys)
        self.render_current_car_initial()
        log_event("ACTION", "Switched to previous car.")

    def next_car(self):
        self.current_index = (self.current_index + 1) % len(self.car_keys)
        self.render_current_car_initial()
        log_event("ACTION", "Switched to next car.")

    def start_monitoring(self):
        self.timer.start()
        self.start_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)
        log_event("ACTION", "Started monitoring cycle.")

    def pause_monitoring(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        log_event("ACTION", "Paused monitoring cycle.")

    def change_interval(self, value):
        self.timer.setInterval(value * 1000)
        log_event("ACTION", "Changed interval of measurement.")

    def update_cycle(self):
        # generate data for current car and update table + log
        key = self.car_keys[self.current_index]
        profile = self.profiles[key]

        sensors = generate_sensor_data(profile)
        faults = check_faults(profile, sensors)
        log_entry(key, sensors, faults)


        # update header and title coloring
        if faults:
            log_event("FAULT", f"Fault(s) detected for {key}: {len(faults)} issues logged.")
        else:
            log_event("SYSTEM OK", f"Cycle completed for {key}. No faults detected.")

        self.car_label.setText(f"{profile['make']} {profile['model']} — {key} ({profile['year']})")

        # write values to table and color-code each cell
        for row, (param, label) in enumerate(COLUMNS):
            value = sensors.get(param, "N/A")
            item_val = QTableWidgetItem(str(value))
            item_val.setTextAlignment(Qt.AlignCenter)

            # default colors
            bg = QColor(200, 255, 200)   # greenish
            fg = QColor(0, 0, 0)

            # determine color based on thresholds and param type
            thr = profile['thresholds']

            # numeric comparisons (must handle missing keys gracefully)
            try:
                if param == "battery_voltage":
                    v = float(value)
                    if v < thr['battery_voltage_min'] or v > thr['battery_voltage_max']:
                        bg = QColor(255, 120, 120)  # red
                    elif v < thr['battery_voltage_min'] + 0.5:
                        bg = QColor(255, 220, 120)  # yellow
                elif param == "oil_pressure":
                    v = float(value)
                    if v < thr['oil_pressure']:
                        bg = QColor(255, 120, 120)  # red
                elif param == "temperature":
                    v = float(value)
                    if v > thr['temperature']:
                        bg = QColor(255, 120, 120)
                    elif v > thr['temperature'] - 5:
                        bg = QColor(255, 220, 120)
                elif param == "rpm":
                    v = float(value)
                    if v > thr['rpm']:
                        bg = QColor(255, 120, 120)
                elif param == "fuel_efficiency":
                    v = float(value)
                    if v < thr['fuel_efficiency_min']:
                        bg = QColor(255, 120, 120)
                elif param == "vibration_level":
                    v = float(value)
                    if v > thr['vibration_level']:
                        bg = QColor(255, 120, 120)
                elif param == "emission_level":
                    v = float(value)
                    if v > thr['emission_level']:
                        bg = QColor(255, 120, 120)
                elif param == "engine_load":
                    v = float(value)
                    if v > thr['engine_load']:
                        bg = QColor(255, 120, 120)
                elif param == "intake_pressure":
                    v = float(value)
                    if v > thr['intake_pressure']:
                        bg = QColor(255, 120, 120)
                elif param == "throttle_position":
                    v = float(value)
                    if v > thr['throttle_position']:
                        bg = QColor(255, 220, 120)
                elif param == "air_fuel_ratio":
                    v = float(value)
                    if v < thr['air_fuel_ratio_min'] or v > thr['air_fuel_ratio_max']:
                        bg = QColor(255, 120, 120)
                else:
                    # default: leave green
                    pass
            except Exception:
                # if any conversion fails, leave default coloring and text
                pass

            item_val.setBackground(bg)
            item_val.setForeground(fg)
            self.table.setItem(row, 1, item_val)

    def closeEvent(self, event):
        # prompt on exit if timer running
        if self.timer.isActive():
            r = QMessageBox.question(self, "Exit", "Monitoring is running. Stop and exit?",
                                     QMessageBox.Yes | QMessageBox.No)
            if r == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = EngineMonitorApp()
    w.show()
    sys.exit(app.exec_())
