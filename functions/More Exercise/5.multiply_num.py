#!/usr/bin/env python

if __name__ == "__main__":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    number_of_negatives = 0


    def is_negative(n):
        if n < 0:
            return True
        else:
            return False

    if n1 == 0 or n2 == 0 or n3 == 0:
        print("zero")
    else:
        if is_negative(n1):
            number_of_negatives += 1
        if is_negative(n2):
            number_of_negatives += 1
        if is_negative(n3):
            number_of_negatives += 1

        if number_of_negatives % 2 == 0:
            print("positive")
        else:
            print("negative")
