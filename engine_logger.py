# engine_logger.py
# Appends telemetry snapshots to a JSON logfile.

import json
from datetime import datetime
import os

LOG_PATH = "engine_log.json"

def log_entry(car_number, sensors, faults):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "car_number": car_number,
        "sensors": sensors,
        "faults": faults
    }

    try:
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, "r") as f:
                data = json.load(f)
        else:
            data = []
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    data.append(entry)

    with open(LOG_PATH, "w") as f:
        json.dump(data, f, indent=2)
