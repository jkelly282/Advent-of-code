import logging

import day2

if __name__ == '__main__':
    args = day2.parse_args()
    try:
        mylines = day2.open_file(args.teststrings)
    except ValueError:
        logging.error("File should contain lines")
