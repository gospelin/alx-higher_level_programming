#!/usr/bin/python3
from sys import argv


length = len(argv) - 1
word = "arguments"

if length == 0:
    print(f"{length} {word}.")
elif length != 1:
    print(f"{length} {word}:")
else:
    word = "argument"
    print(f"{length} {word}:")

if length >= 1:
    for count, args in enumerate(argv, 0):
        if count == 0:
            continue
        print(f"{count}: {args}")
