#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    length = len(argv) - 1
    operation = 0

    if length != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(exit(1))

    for count, args in enumerate(argv):
        if count == 0:
            continue

        if count == 2:
            sign = argv[count]
            a = int(argv[count - 1])
            b = int(argv[count + 1])

            if sign == '+':
                operation = add(a, b)
                print(f"{a:d} {sign} {b:d} = {operation:d}")
                break
            elif sign == '-':
                operation = sub(a, b)
                print(f"{a:d} {sign} {b:d} = {operation:d}")
                break
            elif sign == '*':
                operation = mul(a, b)
                print(f"{a:d} {sign} {b:d} = {operation:d}")
                break
            elif sign == '/':
                operation = div(a, b)
                print(f"{a:d} {sign} {b:d} = {operation:d}")
                break
            else:
                print(f"Unknown operator. Available operators: +, -, * and /")
                print(exit(1))
                break


if __name__ == '__main__':
    main()
