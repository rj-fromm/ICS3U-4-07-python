#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program determines if year is a leap year

import math

counter = 1000


def main():

    for counter in range(1000, 2000):
        if counter % 5 == 0:
            print(counter, counter + 1, counter + 2, counter + 3, counter + 4)

    print("2000")


if __name__ == "__main__":
    main()
