# telemetry_sim.py
# Generates simulated sensor readings from a car profile.

import random

def generate_sensor_data(profile):
    """Return a dict of sensor readings based on profile['sensors'] ranges."""
    s = profile["sensors"]
    readings = {
        "temperature": round(s["temp_base"] + random.uniform(*s["temp_spread"]), 1),
        "oil_pressure": round(random.uniform(*s["oil_range"]), 1),
        "rpm": int(random.uniform(*s["rpm_range"])),
        "coolant_level": round(random.uniform(*s["coolant_range"]), 1),
        "battery_voltage": round(random.uniform(*s["battery_range"]), 2),
        "fuel_efficiency": round(random.uniform(*s["fuel_eff_range"]), 1),
        "vibration_level": round(random.uniform(*s["vibration_range"]), 2),
        "emission_level": round(random.uniform(*s["emission_range"]), 2),
        "engine_load": round(random.uniform(*s["load_range"]), 1),
        "intake_pressure": round(random.uniform(*s["intake_range"]), 1),
        "throttle_position": round(random.uniform(*s["throttle_range"]), 1),
        "air_fuel_ratio": round(random.uniform(*s["afr_range"]), 2)
    }
    return readings
