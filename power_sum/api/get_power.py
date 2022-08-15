from classes import PowerPlant
from urllib import response
import requests
import json


def get_power(power_plant: PowerPlant, from_date: str, to_date: str):
    method = power_plant.method.lower()

    # TODO : Handle exceptions
    if method == "hawes":
        print("toto")
        return get_power_hawes(from_date, to_date)
    elif method == "barnsley":
        print("tata")
        # return get_power_barnsley(from_date, to_date)
    elif method == "hounslow":
        print("titi")
        # return get_power_hounslow(from_date, to_date)
    else:
        return None


def get_power_hawes(from_date: str, to_date: str):
    url = "https://interview.beta.bcmenergy.fr/barnsley"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    unserialized_data = json.loads(response.text)
    formatted_data = [
        {"start": row["start_time"], "end": row["end_time"], "power": row["value"]}
        for row in unserialized_data
    ]
    print(formatted_data)
