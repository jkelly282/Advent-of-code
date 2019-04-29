import collections
import logging
from datetime import datetime

import pandas as pd

import day2


def time_parse(line):
    time = line[1:17]
    map(int, time)
    return time


def parse_guard_name(line):
    guard_id = line[26:30]
    return guard_id


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
    return d2 - d1


def parse_list_chronological_date():
    guard_shifts = pd.read_csv("guard_shifts.csv", sep="\t", names=["Time", "Activity"])
    pd.period_range('1516-01-01', '1518-12-31', freq='D')
    guard_shifts["Time"] = pd.to_datetime(guard_shifts["Time"], format="[%Y-%m-%d %H:%M]")
    guard_shifts.sort_values('Time', inplace=True)
    print(guard_shifts)


if __name__ == '__main__':

    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
    mylines.sort()
    parse_list_chronological_date()

    timeasleep = collections.defaultdict(int)
    guard_id = ""
    d1 = 0
    d2 = 0
    for line in mylines:
        if '#' in line:
            guard = parse_guard_name(line)
            timeasleep[guard]
        elif "falls" in line:
            d1 = time_parse(line)
        elif "wakes" in line:
            d2 = time_parse(line)
            sleep = days_between(d1, d2)
            print(sleep)
