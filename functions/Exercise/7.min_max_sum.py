#!/usr/bin/env python

if __name__ == "__main__":
    numbers = map(int, input().split())
    numbers = sorted(numbers)
    print(f"The minimum number is {numbers[0]}")
    print(f"The maximum number is {numbers[-1]}")
    print(f"The sum number is: {sum(numbers)}")
