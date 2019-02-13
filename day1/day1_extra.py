import argparse
import logging


def open_file(filepath):
    with open(filepath) as f:
        return [int(item.strip()) for item in f]


def parse_args():
    parser = argparse.ArgumentParser(description="Day 2 of AdventOfCode")
    parser.add_argument('-s', dest='santa_file', required=True, help='newline separated file containing integers')
    args = parser.parse_args()
    return args

def find_duplicate():
    running_total = 0
    duplicates = []
    # generate a cumulative total array
    cumulative_total = set()
    solved = False
    while True:
        for i in mylist:
            if running_total in cumulative_total:
                print(running_total)
                solved = True
                break
            else:
                cumulative_total.add(running_total)
        if solved:
            break
    return(running_total)

if __name__ == '__main__':
    args = parse_args()
    try:
        mylist = open_file(args.santa_file)
    except ValueError:
        logging.error("File should only contain valid integers")
    else:
        print("I can't find the file! ")
    duplicate = find_duplicate()
    print(duplicate)
