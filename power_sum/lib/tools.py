# from_date = datetime.fromtimestamp(from_stamp).strftime("%d-%m-%Y")
# to_date = datetime.fromtimestamp(to_stamp).strftime("%d-%m-%Y")
from classes.PowerInterval import PowerInterval


def interpolate_power_intervals(
    power_intervals: list[PowerInterval], interval: int
) -> list[PowerInterval]:
    pass
