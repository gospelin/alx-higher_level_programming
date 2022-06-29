#!/usr/bin/python3

for number in range(100):
    if number != 99:
        print(f"{number:02}, ", end='')
    else:
       print(f"{number:02}")
