from classes import PowerPlant, PowerInterval
import requests
import json


def is_valid_date(date: str):
    # TODO : check if format is valid
    return True


def get_power_intervals(
    power_plant: PowerPlant, from_date: str, to_date: str
) -> list[PowerInterval]:
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


def get_power_hawes(from_date: str, to_date: str) -> list[PowerInterval]:
    url = "https://interview.beta.bcmenergy.fr/hawes"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    unserialized_data = json.loads(response.text)
    formatted_data = [
        PowerInterval(int(row["start"]), int(row["end"]), float(row["power"]))
        for row in unserialized_data
    ]

    return formatted_data


def get_power_barnsley(from_date: str, to_date: str) -> list[PowerInterval]:
    url = "https://interview.beta.bcmenergy.fr/barnsley"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    unserialized_data = json.loads(response.text)
    formatted_data = [
        PowerInterval(int(row["start_time"]), int(row["end_time"]), float(row["value"]))
        for row in unserialized_data
    ]

    return formatted_data


def get_power_hounslow(from_date: str, to_date: str) -> list[PowerInterval]:
    url = "https://interview.beta.bcmenergy.fr/hounslow"
    params = {"from": from_date, "to": to_date}

    response = requests.get(url=url, params=params)

    splitted_lines = response.text.splitlines()
    splitted_lines.pop(0)
    unserialized_data = [line.split(",") for line in splitted_lines]
    formatted_data = [
        PowerInterval(int(row[0]), int(row[1]), float(row[1]))
        for row in unserialized_data
    ]

    return formatted_data
