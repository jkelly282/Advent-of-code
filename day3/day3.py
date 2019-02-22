import logging
import re

import numpy as np

import day2


def parse_claims(mylines):
    '''
    Parses the elves claims

    :param mylines: A list object containing the fabric claims as separate entities
    to be parsed in the format (#int @ int,int: int x int)
    :return: For each entity in the original list this function converts them to [['str','str','str','str']]
    '''
    fabric_coordinates = []
    for i in mylines:
        # gets rid of the empty spaces
        j = i.replace(' ', '')
        parsed_claim = re.split('#|@|,|:|x', j)
        # remove the #claim
        fabric_coordinates.append(parsed_claim[1:6])
    return fabric_coordinates


def parse_fabric_list(claims):
    '''
    Puts the elves claims into an array object

    :param claims: a list object made up of lists in the format [['str','str','str','str'],['str','str','str','str']]
    :return: the overall number of inches (int) which overlap in the making of Santa's magic suit
    '''
    santa_fabric = np.zeros((1000, 1000))
    for i in claims:
        # converting the list of strings to int
        i = list(map(int, i[1:5]))
        santa_fabric[i[1]:i[1] + i[3], i[0]:i[0] + i[2]] += 1
    return np.sum(santa_fabric > 1), santa_fabric


def uncontested_claim(fabric_map: list) -> int:
    '''
    Checks for claims in the fabric which do not overlap with other claims

    :param fabric_map: an array containing the submitted elf claims for santa's fabric:
    :return: the claim that does not conflict with another elf's claim
    '''
    for i in claims:
        i = list(map(int, i))
        a, b, c, d, e = i
        if np.all(fabric_map[c:c + e, b:b + d] == 1):
            return a


if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
        raise

    claims = parse_claims(mylines)
    fabric = parse_fabric_list(claims)
    print(fabric[0])
    winning_claim = uncontested_claim(fabric[1])
    print(winning_claim)
