#!/usr/bin/python3
from sys import argv


def main():
    sum = 0

    for count, args in enumerate(argv):
        if count == 0:
            continue

        sum += int(args)

    print(f"{sum:d}")


if __name__ == '__main__':
    main()
