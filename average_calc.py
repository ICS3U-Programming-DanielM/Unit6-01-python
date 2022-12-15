#!/usr/bin/env python3
# Created by: Daniel Momoh
# Created on: Dec. 14, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the average to the console
import constants
import random


def main():
    # Initiates the sum and counter
    sum = 0
    counter = 0
    # declaring the list
    list_of_integer = []

    # display opening message to console
    print(
        "This program generates a list of random "
        "numbers between 0 and 100, and calculates the average."
    )
    print("")

    # displays random numbers
    for counter in range(constants.MAX_ARRAY_SIZE):
        list_of_integer.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        sum = sum + list_of_integer[counter]
        print(
            "{} added to the list at "
            "position {}".format(list_of_integer[counter], counter)
        )
    # calculates and display average
    for counter in range(1):
        average = sum / constants.MAX_ARRAY_SIZE
        print("")
        print("The average is {:.2f}".format(average))


if __name__ == "__main__":
    main()
