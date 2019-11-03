#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program adds positive numbers


def main():
    # This function adds positive numbers
    counter = 0
    zero = 0
    result = 0

    # Input, Process and Output
    try:
        counter = input("how many numbers do you want to add: ")
        counter = int(counter)
        for zero in range(1, counter + 1):
            usernumber = input("enter a number to add: ")
            usernumber = int(usernumber)
            if usernumber <= 0:
                continue
            else:
                result = usernumber + result
        print(result)
    except(Exception):
        print("Wrong input!!!")

if __name__ == "__main__":
    main()
a