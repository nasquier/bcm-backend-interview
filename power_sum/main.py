import json
from api import get_power_intervals
from lib import interpolate_power_intervals, sum_power_intervals
from classes import PowerPlant, PowerInterval
from datetime import datetime
import csv
import os


root_path = os.path.dirname(os.path.realpath(__file__))
power_plant_file = f"{root_path}/power_plant_list.csv"


def get_power_plants():
    with open(power_plant_file, "r") as csvfile:
        power_plant_iterator = csv.reader(csvfile, delimiter=",", quotechar="|")

        # TODO : Detect which column is the right one for each field, as we don't use a DB here
        # Get fields and skip to actual data
        col_id = 0
        col_name = 1
        col_interval = 2
        col_method = 3
        next(power_plant_iterator)

        power_plants = [
            PowerPlant(
                int(row[col_id]),
                str(row[col_name]),
                int(row[col_interval]),
                str(row[col_method]),
            )
            for row in power_plant_iterator
        ]
        return power_plants


def format_output(power_intervals: PowerInterval, output_format: str):
    final_list = [power_interval.get_dict() for power_interval in power_intervals]
    if output_format == "json":
        output_string = json.dumps(final_list)
    elif output_format == "csv":
        output_string = ";".join(
            ["start,end,power"]
            + [
                ",".join([str(row["start"]), str(row["end"]), str(row["power"])])
                for row in final_list
            ]
        )
    return output_string


def run():
    print("----- Somme des puissances des centrales par intervalles de 15 min -----")
    from_date = input(
        "\nDate de début des intervalles à surveiller au format DD-MM-YYYY (from) : "
    )
    to_date = input(
        "\nDate de fin des intervalles à surveiller au format DD-MM-YYYY (to) : "
    )
    output_format = input("\nFormat voulu en sortie (Pour le moment : json | csv) : ")

    power_plants = get_power_plants()

    all_power_intervals = []
    for power_plant in power_plants:
        # Get power interavls for this power plant
        power_intervals = get_power_intervals(power_plant, from_date, to_date)
        #  Look for missing data and interpolate
        interpolate_power_intervals(power_intervals, power_plant.interval)
        #  Stock them for later
        all_power_intervals += power_intervals

    # Sum all intervals across power_plants
    summed_power_intervals = sum_power_intervals(all_power_intervals, 15 * 60)

    # Format ouput
    output_string = format_output(summed_power_intervals, output_format)
    print(output_string)


if __name__ == "__main__":
    run()
