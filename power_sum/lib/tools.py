from classes import PowerInterval
from datetime import datetime, timedelta


def interpolate_power_intervals(
    power_intervals: list[PowerInterval], interval: int
) -> list[PowerInterval]:
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
