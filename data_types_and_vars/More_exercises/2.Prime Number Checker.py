#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    isPrime = True
    for number in range(2, n):
        if n % number == 0:
            print('False')
            isPrime = False
            break
    if isPrime:
        print('True')