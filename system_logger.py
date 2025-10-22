from datetime import datetime
LOG_FILE = "system_logs.log"
def log_event(action, message):
    timestamp = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} {action}: {message}\n")