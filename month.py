# !/usr/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Nov 2020
# This program will tell u the month if you input  number from 1-12

def main():

    # input
    user_number = int(input("enter a number from 1-12:"))

    # process/ output
    if user_number == 1:
        print(" the month is january ")
    elif user_number == 2:
        print(" the month is february ")
    elif user_number == 3:
        print(" the month is March ")
    elif user_number == 4:
        print(" the month is april ")
    elif user_number == 5:
        print(" the month is May ")
    elif user_number == 6:
        print(" the month is June ")
    elif user_number == 7:
        print(" the month is july ")
    elif user_number == 8:
        print(" the month is Augest ")
    elif user_number == 9:
        print(" the month is September ")
    elif user_number == 10:
        print(" the month is October ")
    elif user_number == 11:
        print(" the month is November ")
    elif user_number == 12:
        print(" the month is december ")
    else:
        print(" this number does not have a month ")


if __name__ == "__main__":
    main()
