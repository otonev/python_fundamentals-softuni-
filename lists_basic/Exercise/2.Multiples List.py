#!/usr/bin/env python

if __name__ == "__main__":
    factor=int(input())
    count=int(input())
    nums = []
    for i in range(factor,count*factor+1,factor):
        nums.append(i)
    print(nums)
    