#!/usr/bin/env python

if __name__ == "__main__":
    METERS_IN_KILOMETER = 1000
    meters = int(input())
    kilometers = meters / METERS_IN_KILOMETER
    print(f'{kilometers:.2f}')
    