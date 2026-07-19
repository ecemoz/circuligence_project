#Ürünün kusurlu olup olmadığını belirleyelim.

import random 

from simulator.config import MACHINE_CONFIG

def calculate_defect_risk(machine_state: dict) -> float:


    risk = 0.03

    for parameter, value in machine_state.items():
        config = MACHINE_CONFIG[parameter]
        
        normal_min = config["normal_min"]
        normal_max = config["normal_max"]

        if value < normal_min:
            risk += 0.10
        
        elif value > normal_max:
            risk += 0.10
        
    if (
        machine_state["melt_temperature"] > 240 and machine_state["injection_speed"] > 1.00
        ):
        risk += 0.20
        

    if (
        machine_state["cooling_time"] < 7 and machine_state["melt_temperature"] > 240
        ):
        risk += 0.25
        
    return min(risk, 0.95) 

def generate_defect(machine_state: dict) -> dict:

    defect_risk = calculate_defect_risk(machine_state)
    is_defective = random.random() < defect_risk

    return {
        "is_defective" : is_defective,
        "defect_risk" : round(defect_risk, 2)
    }

if __name__ == "__main__":

    test_machine_state = {
        "melt_temperature": 250,
        "mold_temperature": 35,
        "injection_pressure": 1.05,
        "injection_speed": 1.10,
        "cooling_time": 6.0,
        "cycle_time": 22,
    }

    result = generate_defect(test_machine_state)

    print("Makine durumu:")
    print(test_machine_state)
    print("Kusur sonucu:")
    print(result)

    