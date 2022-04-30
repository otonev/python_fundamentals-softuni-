#!/usr/bin/env python

if __name__ == "__main__":
    def check_even(number):
        if number % 2 == 0:
            return True

        return False


    numbers = map(int, input().split())
    even_numbers = list(filter(check_even, numbers))
    print(even_numbers)
    