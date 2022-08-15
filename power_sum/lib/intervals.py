from classes import PowerInterval
from datetime import datetime, timedelta
from math import floor


def interpolate_power_intervals(power_intervals: list[PowerInterval], interval: int):
    last_interval = power_intervals[0]
    index = 1
    while index < len(power_intervals):
        power_interval = power_intervals[index]
        last_end_datetime = datetime.fromtimestamp(last_interval.end)
        start_datetime = datetime.fromtimestamp(power_interval.start)

        difference = start_datetime - last_end_datetime
        #  Here we tolerate a slight desync. Don't know it it's ok
        if difference.seconds > interval:
            power_intervals.insert(
                index,
                PowerInterval(
                    last_interval.end,
                    int(
                        datetime.timestamp(
                            last_end_datetime + timedelta(seconds=interval)
                        )
                    ),
                    floor((last_interval.power + power_interval.power) / 2),
                ),
            )
            index += 1

        index += 1
        last_interval = power_interval


def sum_power_intervals(
    power_intervals: list[PowerInterval], interval: int
) -> list[PowerInterval]:
    # TODO : What should we take as a reference value? Do we sum based on interval's start or end? Or should we extrapolate data based on the wanted interval (out of scope) ?
    summed_power_intervals: list[PowerInterval] = []
    for power_interval in power_intervals:
        # We look for all intervals ending with the same timestamp
        index = next(
            (
                i
                for i, interval in enumerate(summed_power_intervals)
                if interval.end == power_interval.end
            ),
            None,
        )
        # If it doesn't exist, we create an interval based on this timestamp, but we create the start date with the wanted length (for this exercise : 15 min)
        if index is None:
            summed_power_intervals.append(
                PowerInterval(
                    int(
                        datetime.timestamp(
                            datetime.fromtimestamp(power_interval.end)
                            - timedelta(seconds=interval)
                        )
                    ),
                    power_interval.end,
                    power_interval.power,
                )
            )
        else:
            summed_power_intervals[index].power += power_interval.power

    # Sort
    summed_power_intervals.sort(key=lambda power_interval: power_interval.start)
    return summed_power_intervals
