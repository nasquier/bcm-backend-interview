from classes import PowerInterval
from datetime import datetime, timedelta


def interpolate_power_intervals(power_intervals: list[PowerInterval], interval: int):
    last_interval = power_intervals[0]
    index = 1
    while index < len(power_intervals):
        power_interval = power_intervals[index]
        last_end_datetime = datetime.fromtimestamp(last_interval.end)
        start_datetime = datetime.fromtimestamp(power_interval.start)

        difference = start_datetime - last_end_datetime
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
                    (last_interval.power + power_interval.power) / 2,
                ),
            )
            index += 1

        index += 1
        last_interval = power_interval


def sum_power_intervals(
    power_intervals: list[PowerInterval], interval: int
) -> list[PowerInterval]:
    summed_power_intervals: list[PowerInterval] = []
    for power_interval in power_intervals:
        index = next(
            (
                i
                for i, interval in enumerate(summed_power_intervals)
                if interval.end == power_interval.end
            ),
            None,
        )
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

    summed_power_intervals.sort(key=lambda power_interval: power_interval.start)
    return summed_power_intervals
