import logging
import re

import day2


def parse_claims(mylines):
    fabric_coordinates = []
    for i in mylines:
        parsed_claim = re.split('@|,|:|x', i)
        fabric_coordinates.append(parsed_claim)
    return fabric_coordinates



if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.teststrings)
    except ValueError:
        logging.error("File should contain lines")
