#!/usr/bin/env python

if __name__ == "__main__":
    def aliquot_sum(n):
        sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                sum += i

        return sum

    n = int(input())
    if aliquot_sum(n) / 2 == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
