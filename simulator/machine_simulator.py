#Her üretim çevrimi için makine parametreleri üreteceğiz.

import random 

from simulator.config import MACHINE_CONFIG


def generate_machine_state() -> dict:

    machine_state = {
        "melt_temperature": round(
            random.uniform(
                MACHINE_CONFIG["melt_temperature"]["normal_min"],
                MACHINE_CONFIG["melt_temperature"]["normal_max"]
            ),
            2,
        ),

        "mold_temperature": round(
            random.uniform(
                MACHINE_CONFIG["mold_temperature"]["normal_min"],
                MACHINE_CONFIG["mold_temperature"]["normal_max"]
            ),
            2,
        ),

        "injection_pressure": round(
            random.uniform(
                MACHINE_CONFIG["injection_pressure"]["normal_min"],
                MACHINE_CONFIG["injection_pressure"]["normal_max"]
            ),
            2,
        ),

        "injection_speed": round(
            random.uniform(
                MACHINE_CONFIG["injection_speed"]["normal_min"],
                MACHINE_CONFIG["injection_speed"]["normal_max"]
            ),
            2,
        ),

        "cooling_time": round(
            random.uniform(
                MACHINE_CONFIG["cooling_time"]["normal_min"],
                MACHINE_CONFIG["cooling_time"]["normal_max"]
            ),
            2,
        ),

        "cycle_time": round(
            random.uniform(
                MACHINE_CONFIG["cycle_time"]["normal_min"],
                MACHINE_CONFIG["cycle_time"]["normal_max"]
            ),
            2,
        ),
    }

    return machine_state


if __name__ == "__main__":
    state = generate_machine_state()
    print("Üretilen makine durumu:")
    print(state)


