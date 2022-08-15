from datetime import datetime
from classes import PowerPlant


def get_power(power_plant: PowerPlant, from_stamp: int, to_stamp: int):
    method = power_plant.method.lower()

    # TODO : Handle exceptions
    if method == "hawes":
        print("toto")
        # return get_power_hawes(from_stamp, to_stamp)
    if method == "barnsley":
        print("tata")
        # return get_power_barnsley(from_stamp, to_stamp)
    if method == "hounslow":
        print("titi")
        # return get_power_hounslow(from_stamp, to_stamp)
