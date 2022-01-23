#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    for num in range(1, n + 1):
        sum_of_digs = 0
        digits = num
        while digits > 0:
            sum_of_digs += digits % 10
            digits = int(digits / 10)
        if (sum_of_digs == 5) or (sum_of_digs == 7) or (sum_of_digs == 11):
            print(f'{num} -> True')
        else:
            print(f'{num} -> False')