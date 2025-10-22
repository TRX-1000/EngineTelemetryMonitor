# car_profiles.py
# Detailed car profiles used by the telemetry simulator and fault checker.

CAR_PROFILES = {
    "KA01AB1234": {
        "make": "Mercedes",
        "model": "C200",
        "year": 2021,
        "thresholds": {
            "temperature": 110,
            "oil_pressure": 25,
            "rpm": 6500,
            "coolant_level": 30,
            "battery_voltage_min": 11.8,
            "battery_voltage_max": 14.8,
            "fuel_efficiency_min": 8.0,
            "vibration_level": 5.0,
            "emission_level": 1.5,
            "engine_load": 90,
            "intake_pressure": 250,
            "throttle_position": 95,
            "air_fuel_ratio_min": 12.0,
            "air_fuel_ratio_max": 15.5
        },
        "sensors": {
            "temp_base": 90,
            "temp_spread": (-5, 15),
            "oil_range": (20, 60),
            "rpm_range": (800, 7000),
            "coolant_range": (30, 100),
            "battery_range": (12.0, 15.0),
            "fuel_eff_range": (6.0, 15.0),
            "vibration_range": (1.0, 6.0),
            "emission_range": (0.8, 2.0),
            "load_range": (20, 100),
            "intake_range": (80, 260),
            "throttle_range": (0, 100),
            "afr_range": (11.5, 16.0)
        }
    },

    "KA05CD5678": {
        "make": "BMW",
        "model": "320i",
        "year": 2019,
        "thresholds": {
            "temperature": 115,
            "oil_pressure": 22,
            "rpm": 7000,
            "coolant_level": 25,
            "battery_voltage_min": 11.5,
            "battery_voltage_max": 15.0,
            "fuel_efficiency_min": 7.0,
            "vibration_level": 5.5,
            "emission_level": 1.6,
            "engine_load": 88,
            "intake_pressure": 240,
            "throttle_position": 94,
            "air_fuel_ratio_min": 11.8,
            "air_fuel_ratio_max": 15.2
        },
        "sensors": {
            "temp_base": 92,
            "temp_spread": (-6, 18),
            "oil_range": (18, 58),
            "rpm_range": (900, 7200),
            "coolant_range": (25, 100),
            "battery_range": (12.0, 14.8),
            "fuel_eff_range": (7.0, 14.0),
            "vibration_range": (1.2, 6.2),
            "emission_range": (0.9, 2.2),
            "load_range": (25, 95),
            "intake_range": (90, 255),
            "throttle_range": (0, 100),
            "afr_range": (11.5, 15.5)
        }
    },

    "KA09EF9101": {
        "make": "Porsche",
        "model": "911 GT3 RS",
        "year": 2023,
        "thresholds": {
            "temperature": 108,
            "oil_pressure": 28,
            "rpm": 9000,
            "coolant_level": 35,
            "battery_voltage_min": 11.9,
            "battery_voltage_max": 14.9,
            "fuel_efficiency_min": 6.5,
            "vibration_level": 6.0,
            "emission_level": 1.3,
            "engine_load": 95,
            "intake_pressure": 245,
            "throttle_position": 98,
            "air_fuel_ratio_min": 12.2,
            "air_fuel_ratio_max": 15.0
        },
        "sensors": {
            "temp_base": 94,
            "temp_spread": (-4, 20),
            "oil_range": (25, 65),
            "rpm_range": (1000, 9500),
            "coolant_range": (30, 100),
            "battery_range": (12.0, 15.0),
            "fuel_eff_range": (5.5, 10.0),
            "vibration_range": (1.0, 7.0),
            "emission_range": (0.7, 1.9),
            "load_range": (30, 100),
            "intake_range": (100, 260),
            "throttle_range": (0, 100),
            "afr_range": (11.8, 15.3)
        }
    },

    "KA03GH4567": {
        "make": "McLaren",
        "model": "720S",
        "year": 2022,
        "thresholds": {
            "temperature": 110,
            "oil_pressure": 30,
            "rpm": 8200,
            "coolant_level": 33,
            "battery_voltage_min": 11.7,
            "battery_voltage_max": 14.7,
            "fuel_efficiency_min": 5.5,
            "vibration_level": 5.8,
            "emission_level": 1.7,
            "engine_load": 92,
            "intake_pressure": 255,
            "throttle_position": 97,
            "air_fuel_ratio_min": 12.0,
            "air_fuel_ratio_max": 15.5
        },
        "sensors": {
            "temp_base": 93,
            "temp_spread": (-5, 17),
            "oil_range": (20, 62),
            "rpm_range": (1000, 8500),
            "coolant_range": (25, 100),
            "battery_range": (12.0, 14.9),
            "fuel_eff_range": (4.5, 9.5),
            "vibration_range": (1.0, 6.5),
            "emission_range": (0.8, 2.0),
            "load_range": (25, 100),
            "intake_range": (90, 260),
            "throttle_range": (0, 100),
            "afr_range": (11.7, 15.4)
        }
    },

    "KA02JK2468": {
        "make": "Ferrari",
        "model": "F8 Tributo",
        "year": 2022,
        "thresholds": {
            "temperature": 109,
            "oil_pressure": 29,
            "rpm": 8000,
            "coolant_level": 32,
            "battery_voltage_min": 11.8,
            "battery_voltage_max": 14.8,
            "fuel_efficiency_min": 6.0,
            "vibration_level": 5.6,
            "emission_level": 1.4,
            "engine_load": 93,
            "intake_pressure": 250,
            "throttle_position": 96,
            "air_fuel_ratio_min": 12.1,
            "air_fuel_ratio_max": 15.4
        },
        "sensors": {
            "temp_base": 91,
            "temp_spread": (-5, 18),
            "oil_range": (22, 60),
            "rpm_range": (900, 8300),
            "coolant_range": (30, 100),
            "battery_range": (12.0, 14.8),
            "fuel_eff_range": (5.5, 10.0),
            "vibration_range": (1.0, 6.5),
            "emission_range": (0.7, 1.9),
            "load_range": (20, 100),
            "intake_range": (85, 255),
            "throttle_range": (0, 100),
            "afr_range": (11.8, 15.5)
        }
    }
}
