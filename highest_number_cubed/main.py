"""This is the entry point of the program."""


def highest_number_cubed(limit):
    number = 0
    while number ** 3 <= limit:
        number += 1
    return number - 1