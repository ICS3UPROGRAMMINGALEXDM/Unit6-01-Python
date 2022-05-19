#!/usr/bin/env python3

import random

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Generates 10 random numbers and calculates the average
import constants


def main():
    num_arr = []
    for counter in range(constants.MAX_SIZE):
        rand_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        num_arr.append(rand_num)
        print("Position {} is {}".format(counter, num_arr[counter]))
    sum_num = 0
    for counter in range(constants.MAX_SIZE):
        sum_num += num_arr[counter]
    avg = sum_num / constants.MAX_SIZE

    print("\nThe average is {}".format(avg))


if __name__ == "__main__":
    main()
