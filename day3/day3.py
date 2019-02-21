import logging
import re

import numpy as np

import day2


def parse_claims(mylines):
    fabric_coordinates = []
    for i in mylines:
        # gets rid of the empty spaces
        j = i.replace(' ', '')
        parsed_claim = re.split('@|,|:|x', j)
        #remove the #claim
        fabric_coordinates.append(parsed_claim[1:5])
    return fabric_coordinates


def parse_fabric_list(claims):
    santa_fabric = np.zeros((1000, 1000))
    claimed_inches = 0
    for i in claims:
        # converting the list of strings to int
        i = list(map(int, i))
        santa_fabric[i[1]:i[1] + i[3], i[0]:i[0] + i[2]] += 1
    return np.sum(santa_fabric > 1)


if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
    claims = parse_claims(mylines)
    fabric = parse_fabric_list(claims)
    print(fabric)
