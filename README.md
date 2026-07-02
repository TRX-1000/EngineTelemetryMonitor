# EngineTelemetryMonitor

A Python-based engine telemetry monitoring system that simulates automotive 
ECU diagnostic functionality.

## Overview

Monitors real-time simulated sensor data across multiple vehicle profiles, 
detects threshold violations to generate fault codes — inspired by automotive 
Diagnostic Trouble Code (DTC) systems — and maintains persistent logs. 
Mirrors core functionality found in real automotive ECU diagnostic software.

## Features

- Real-time sensor visualization via a PyQt5 GUI with color-coded fault 
  highlighting (green = normal, yellow = warning, red = fault)
- 5 vehicle profiles with individual threshold configurations per model
- 12 monitored parameters: temperature, oil pressure, RPM, coolant level, 
  battery voltage, fuel efficiency, vibration, emissions, engine load, 
  intake pressure, throttle position, and air-fuel ratio
- Fault detection and persistent JSON logging (inspired by OBD-II DTC systems)
- System activity logging to a `.log` file
- Adjustable monitoring interval (1–10 seconds)
- Modular architecture — simulation, fault detection, logging, and UI 
  separated into independent modules

## Project Structure

| File | Responsibility |
|------|----------------|
| `main.py` | Application entry point |
| `car_profiles.py` | Vehicle data and per-model threshold configuration |
| `telemetry_sim.py` | Simulated sensor data generation |
| `fault_checker.py` | Threshold-based fault detection logic |
| `engine_logger.py` | Persists telemetry and fault data to JSON |
| `system_logger.py` | Logs system-level activity events |
| `engine_monitor.py` | PyQt5 GUI and monitoring cycle |

## Tech Stack

- Python 3
- PyQt5

## Getting Started

**Prerequisites:**
```bash
pip install PyQt5
```

**Run:**
```bash
python main.py
```

## How It Works

1. Select a vehicle profile using the Prev/Next buttons
2. Press Start to begin the monitoring cycle
3. Sensor data is simulated at the configured interval and displayed 
   in real time
4. Any parameter exceeding its threshold is highlighted in red/yellow
5. All readings and faults are logged to `engine_log.json`
6. System events are logged to `system_logs.log`

## Inspiration

Automotive ECU diagnostic systems and the OBD-II Diagnostic Trouble Code 
standard — the same fault detection principles used in real vehicle 
diagnostics tools.