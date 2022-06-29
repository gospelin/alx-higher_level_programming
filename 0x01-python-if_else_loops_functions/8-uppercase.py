#!/usr/bin/python3
def uppercase(str):
    num = 32
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{:c}".format(ord(str[i]) - num), end='')
    print()
