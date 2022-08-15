from classes import PowerPlant
import requests
import json


def get_power(power_plant: PowerPlant, from_date: str, to_date: str):
    method = power_plant.method.lower()

    # TODO : Handle exceptions
    if method == "hawes":
        return get_power_hawes(from_date, to_date)
    elif method == "barnsley":
        return get_power_barnsley(from_date, to_date)
    elif method == "hounslow":
        return get_power_hounslow(from_date, to_date)
    else:
        return None


def get_power_hawes(from_date: str, to_date: str):
    url = "https://interview.beta.bcmenergy.fr/hawes"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    formatted_data = json.loads(response.text)

    return formatted_data


def get_power_barnsley(from_date: str, to_date: str):
    url = "https://interview.beta.bcmenergy.fr/barnsley"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    unserialized_data = json.loads(response.text)
    formatted_data = [
        {"start": row["start_time"], "end": row["end_time"], "power": row["value"]}
        for row in unserialized_data
    ]

    return formatted_data


def get_power_hounslow(from_date: str, to_date: str):
    url = "https://interview.beta.bcmenergy.fr/hounslow"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    unserialized_data = [line.split(",") for line in response.text.splitlines()]
    formatted_data = [
        {"start": row[0], "end": row[1], "power": row[2]} for row in unserialized_data
    ]

    return formatted_data
