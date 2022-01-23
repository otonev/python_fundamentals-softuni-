#!/usr/bin/env python

if __name__ == "__main__":
    divisor = int(input())
    bound = int(input())
    max_n = 0
    for n in range(1, bound + 1):
        if n % divisor == 0:
            max_n = n

    print(max_n)