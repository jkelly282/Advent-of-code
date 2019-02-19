import argparse
import logging

from fuzzywuzzy import fuzz


def open_file(filepath):
    with open(filepath) as f:
        return [str(item.strip()) for item in f]


def parse_args():
    parser = argparse.ArgumentParser(description="Day 2 refactoring")
    parser.add_argument('-f', dest='text_strings', required=True, help="Newline seperated text file")
    args = parser.parse_args()
    return args


def find_checksum(checksum_list):
    chars = "abcdefghijklmnopqrstuvwxyz"
    two = 0
    three = 0  # type: int
    for i in checksum_list:
        two_check = 0  # type: int
        three_check = 0
        for char in chars:
            count = i.count(char)
            if count > 1:
                if count == 2 and two_check == 0:
                    two += 1
                    two_check += 1
                elif count == 3 and three_check == 0:
                    three += 1
                    three_check += 1

    checksum = two * three
    return checksum


def find_similar_strings(string_lines):
    for i in range(len(string_lines)):
        for j in range(i + 1, len(string_lines) - 1):
            ratio_matching = []
            ratio_matching = fuzz.ratio(string_lines[i], string_lines[j])
            test = []
            test.append(ratio_matching)
            percentage_correct = int((len(string_lines[i]) - 1) / len(string_lines[i]) * 100)
            if ratio_matching == percentage_correct:
                return string_lines[j], string_lines[i]


def remove_duplicates(duplicates):
    answer = set(i for i, j in zip(*duplicates) if i == j)
    return answer


if __name__ == '__main__':
    args = parse_args()
    try:
        mylines = open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
    checksum = find_checksum(mylines)
    print(checksum)
    test = find_similar_strings(mylines)
    answer = remove_duplicates(test)
    print(answer)
    print(test)
