#!/usr/bin/python3
def print_last_digit(number):
    lt = int(str(number)[-1])
    print("{:d}".format(lt), end="")
    return lt
