from pip._internal.utils import logging

import day2


def parse_list_chronological_date(date_list):
    '''

    :param date_list:
    :return:
    '''


if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.text_strings)
    except ValueError:
        logging.error("File should contain lines")
        raise
    sorted_lines = parse_list_chronological_date(mylines)
