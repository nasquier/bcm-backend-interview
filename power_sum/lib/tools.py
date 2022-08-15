from classes.PowerInterval import PowerInterval
from datetime import datetime


def interpolate_power_intervals(
    power_intervals: list[PowerInterval], interval: int
) -> list[PowerInterval]:
    last_interval = power_intervals[0]
    for power_interval in power_intervals[1:-1]:
        from_datetime = datetime.fromtimestamp(power_interval.start).strftime(
            "%Y-%m-%d, %H:%M:%S"
        )
        # to_date = datetime.fromtimestamp(to_stamp).strftime("%d-%m-%Y")
        print(from_datetime)
