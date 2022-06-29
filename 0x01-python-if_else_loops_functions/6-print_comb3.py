#!/usr/bin/python3

for number in range(0, 90):
    if number % 10 > number / 10:
        if number != 89:
            print(f"{number:02}, ", end='')
        else:
            print(f"{number:02}")
