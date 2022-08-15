from api import get_power_intervals
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
for power_plant in power_plants:
    print("---" + power_plant.name + "---")
    power_intervals = get_power_intervals(power_plant, "01-01-2020", "02-01-2020")
