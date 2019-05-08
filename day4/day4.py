import logging
from datetime import datetime
import pandas as pd
from day2 import day2

()


def time_parse(line):
    time = line[1:17]
    map(int, time)
    return time

def time_parse_minute(line):
    time = line[15:17]
    map(int, time)
    return(int(time))

def parse_guard_name(line):
    guard_id = line[26:30]
    return guard_id


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
    return d2 - d1

def find_most_frequent(lines, guard):
    guard_number = ""
    minutes_asleep = []
    d1 = 0
    d2 = 0
    for line in lines:
        if '#' in line:
            guard_number = parse_guard_name(line)
        if guard_number == guard:
            print(line)
            if "falls" in line:
                d1 = time_parse_minute(line)
            if "wakes" in line:
                d2 = time_parse_minute(line)
                minutes_asleep += range(d1,d2)
                print(minutes_asleep)
    minutes_asleep_dict = {}
    for i in minutes_asleep:
        if i in minutes_asleep_dict:
            minutes_asleep_dict[i] += 1
        if i not in minutes_asleep_dict:
            minutes_asleep_dict[i] = 1
        sorted_minutes = sorted(minutes_asleep_dict.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_minutes)
        minute_winning = sorted_minutes[0][0]
        answer = int(minute_winning)*int(guard[0:2])
        print(answer)


def find_most_frequent_minute(lines):
    guard_number = ""
    minutes_asleep = []
    d1 = 0
    d2 = 0
    for line in lines:
        if '#' in line:
            guard_number = parse_guard_name(line)
        if guard_number == guard:
            print(line)
            if "falls" in line:
                d1 = time_parse_minute(line)
            if "wakes" in line:
                d2 = time_parse_minute(line)
                minutes_asleep += range(d1,d2)
                print(minutes_asleep)
    minutes_asleep_dict = {}
    for i in minutes_asleep:
        if i in minutes_asleep_dict:
            minutes_asleep_dict[i] += 1
        if i not in minutes_asleep_dict:
            minutes_asleep_dict[i] = 1
        sorted_minutes = sorted(minutes_asleep_dict.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_minutes)
        minute_winning = sorted_minutes[0][0]
        answer = int(minute_winning)*int(guard[0:2])

        print(guard_number)
        print((sorted_minutes[0][0]*int(guard_number[0:3])))










if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
    mylines.sort()

    guard_id = {}
    d1 = 0
    d2 = 0
    guard_number = ""
    for line in mylines:
        if '#' in line:
            guard = parse_guard_name(line)
            if guard not in guard_id:
                guard_number = guard
                guard_id[guard] = 0
            elif guard in guard_id:
                guard_number = guard
        elif "falls" in line:
            d1 = time_parse(line)
        elif "wakes" in line:
            d2 = time_parse(line)
            sleep = days_between(d1, d2)
            guard_id[guard_number] += int((sleep.total_seconds() / 60))
    # print(guard_id)
    sorted_guard = sorted(guard_id.items(), key=lambda kv: kv[1], reverse=True)
    winning = (sorted_guard[0][0])
    find_most_frequent(mylines, winning)
    find_most_frequent_minute(mylines)