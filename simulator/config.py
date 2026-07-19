#Burada fabrikanın normal çalışma aralıklarını söyleyeceğim.

MACHINE_CONFIG = {
    "melt_temperature": {
        "min": 190,
        "normal_min" :  210,
        "normal_max" :  240,
        "max": 260,
        "unit": "C",

    },

    "mold_temperature": {
        "min": 16,
        "normal_min" : 27,
        "normal_max" : 39,
        "max": 54,
        "unit": "C",
    },
    
    "injection_pressure" : {
        "min" : 0.70,
        "normal_min" : 0.85,
        "normal_max" : 1.00,
        "max" : 1.20,
        "unit" : "normalized",

    },

    "injection_speed" : {
        "min" : 0.50,
        "normal_min" : 0.75,
        "normal_max" : 1.00,
        "max" : 1.20,
        "unit" : "normalized",
    },

    "cooling_time" : {
        "min" : 5.0,
        "normal_min" : 7.0,
        "normal_max" : 10.0,
        "max" : 15.0,
        "unit" : "seconds"
    },

    "cycle_time" : {
        "min" : 15.0,
        "normal_min" : 18.0,
        "normal_max" : 24.0,
        "max" : 30.0,
        "unit" : "seconds"
    }
}