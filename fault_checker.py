# fault_checker.py
# Explicit per-parameter fault checking (returns list of human-readable messages).

def check_faults(profile, sensors):
    faults = []
    thr = profile['thresholds']

    # Temperature (high)
    if sensors.get('temperature') is not None and sensors['temperature'] > thr['temperature']:
        faults.append(f"Temperature {sensors['temperature']}°C > {thr['temperature']}°C")

    # Oil pressure (low)
    if sensors.get('oil_pressure') is not None and sensors['oil_pressure'] < thr['oil_pressure']:
        faults.append(f"Oil pressure {sensors['oil_pressure']} PSI < {thr['oil_pressure']} PSI")

    # RPM (over-rev)
    if sensors.get('rpm') is not None and sensors['rpm'] > thr['rpm']:
        faults.append(f"RPM {sensors['rpm']} > {thr['rpm']}")

    # Coolant level (low)
    if sensors.get('coolant_level') is not None and sensors['coolant_level'] < thr['coolant_level']:
        faults.append(f"Coolant level {sensors['coolant_level']}% < {thr['coolant_level']}%")

    # Battery voltage (min/max)
    if sensors.get('battery_voltage') is not None:
        v = sensors['battery_voltage']
        if v < thr['battery_voltage_min'] or v > thr['battery_voltage_max']:
            faults.append(f"Battery voltage {v}V out of range ({thr['battery_voltage_min']}-{thr['battery_voltage_max']}V)")

    # Fuel efficiency (low)
    if sensors.get('fuel_efficiency') is not None and sensors['fuel_efficiency'] < thr['fuel_efficiency_min']:
        faults.append(f"Fuel efficiency {sensors['fuel_efficiency']} km/l < {thr['fuel_efficiency_min']} km/l")

    # Vibration (high)
    if sensors.get('vibration_level') is not None and sensors['vibration_level'] > thr['vibration_level']:
        faults.append(f"Vibration {sensors['vibration_level']} > {thr['vibration_level']}")

    # Emission (high)
    if sensors.get('emission_level') is not None and sensors['emission_level'] > thr['emission_level']:
        faults.append(f"Emission {sensors['emission_level']} > {thr['emission_level']}")

    # Engine load (high)
    if sensors.get('engine_load') is not None and sensors['engine_load'] > thr['engine_load']:
        faults.append(f"Engine load {sensors['engine_load']}% > {thr['engine_load']}%")

    # Intake pressure (high)
    if sensors.get('intake_pressure') is not None and sensors['intake_pressure'] > thr['intake_pressure']:
        faults.append(f"Intake pressure {sensors['intake_pressure']} > {thr['intake_pressure']}")

    # Throttle (high)
    if sensors.get('throttle_position') is not None and sensors['throttle_position'] > thr['throttle_position']:
        faults.append(f"Throttle position {sensors['throttle_position']}% > {thr['throttle_position']}%")

    # Air-Fuel Ratio (out of range)
    if sensors.get('air_fuel_ratio') is not None:
        afr = sensors['air_fuel_ratio']
        if afr < thr['air_fuel_ratio_min'] or afr > thr['air_fuel_ratio_max']:
            faults.append(f"AFR {afr} out of range ({thr['air_fuel_ratio_min']}-{thr['air_fuel_ratio_max']})")

    return faults
