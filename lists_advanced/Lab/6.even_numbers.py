#!/usr/bin/env python
if __name__ == "__main__":
    nums = list(map(int, input().split(", ")))
    even_indexes = [i for i, n in enumerate(nums) if n % 2 == 0]
    print(even_indexes)