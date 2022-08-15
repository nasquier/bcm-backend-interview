import json
from api import get_power_intervals
from lib import interpolate_power_intervals, sum_power_intervals
from classes import PowerPlant
from datetime import datetime
import csv
import os


root_path = os.path.dirname(os.path.realpath(__file__))
power_plant_file = f"{root_path}/power_plant_list.csv"

with open(power_plant_file, "r") as csvfile:
    power_plant_iterator = csv.reader(csvfile, delimiter=",", quotechar="|")

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

all_power_intervals = []
for power_plant in power_plants:
    power_intervals = get_power_intervals(power_plant, "01-01-2020", "02-01-2020")
    interpolate_power_intervals(power_intervals, power_plant.interval)
    all_power_intervals += power_intervals

summed_power_intervals = sum_power_intervals(all_power_intervals, 15 * 60)

final_list = [power_interval.get_dict() for power_interval in summed_power_intervals]
output_format = "csv"
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
print(output_string)
