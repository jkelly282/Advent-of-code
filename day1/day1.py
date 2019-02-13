# Read the variables from the CSV
import argparse
import logging


def open_file(filepath):
    with open(filepath) as f:
        return [int(item.strip()) for item in f]


def parse_args():
    parser = argparse.ArgumentParser(description="Day 1 of AdventOfCode")

    parser.add_argument('-s', dest='santa_file', required=True, help='newline separated file containing integers')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()

    try:
        mylist = open_file(args.santa_file)
    except ValueError:
        logging.error("File should only contain valid integers")
    else:
        print(sum(mylist))
