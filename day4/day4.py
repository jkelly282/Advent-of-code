import logging
import re
from datetime import datetime

def time_parse(line):
    time = line[1:17]
    map(int, time)
    return time


def parse_guard_name(line):
    guard_id = re.split('#', line)
    guard_id = re.split(" ", guard_id[1])
    return guard_id[0]


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M")
    return d2 - d1


def parse_guard_input(lines):
    guard_id = {}
    return_tuple = ()
    d1 = 0
    minutes_asleep = []
    guard_names = []
    guard_number = ""
    for line in lines:
        if '#' in line:
            guard = parse_guard_name(line)
            guard_names.append(guard)
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
            minutes = sleep.total_seconds()
            total_minutes = minutes / 60
            minutes_asleep.append(int(total_minutes))
            guard_id[guard_number] += int(total_minutes)
    return_tuple += guard_id, minutes_asleep, guard_names
    return return_tuple


def part_1(lines):
    guard_id = parse_guard_input(lines)
    guard = guard_id[0]
    sorted_guard = sorted(guard.items(), key=lambda kv: kv[1], reverse=True)
    winning = (sorted_guard[0][0])
    print("The answer for part 1 is", winning)


def find_most_frequent_minute(lines, guard):
    minutes_asleep = parse_guard_input(lines)
    minutes_asleep_dict_frequent_guard = {}
    sorted_minutes = []
    total = []
    for i in minutes_asleep[1]:
        if i in minutes_asleep_dict_frequent_guard:
            minutes_asleep_dict_frequent_guard[i] += 1
        if i not in minutes_asleep_dict_frequent_guard:
            minutes_asleep_dict_frequent_guard[i] = 1
        sorted_minutes = sorted(minutes_asleep_dict_frequent_guard.items(), key=lambda kv: kv[1], reverse=True)
        sorted_minutes.append(guard)
    total.append(sorted_minutes)
    return total


def part_2(guard_ids):
    for i in guard_ids:
        guard_frequent = find_most_frequent_minute(mylines, i)
        guard_sleep_most.append(guard_frequent)
    winning_minute = 0
    winning_time = 0
    for orange in guard_sleep_most:
        try:
            minute = orange[0][0][1]
            if orange[0][0][1] > winning_minute:
                winning_minute = orange[0][0][1]
                winning_time = orange[0][0][0]
                guard_sleep = orange[0][-1]
        except IndexError:
            continue
    answer2 = int(winning_time) * int(guard_sleep)
    print("The answer for part two is", answer2)


if __name__ == '__main__':
    import day2

    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
    mylines.sort()
    part_1(mylines)
    guard_sleep_most = []
    guard_ids = parse_guard_input(mylines)
    part_2(guard_ids[2])
