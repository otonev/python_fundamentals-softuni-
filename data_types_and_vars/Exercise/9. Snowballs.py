#!/usr/bin/env python
import math

if __name__ == "__main__":
    n = int(input())
    max_snowball_value = 0
    max_snowball_snow = 0
    max_snowball_time = 0
    max_snowball_quality = 0
    for snowball in range(n):
        snowballSnow = int(input())
        snowballTime = int(input())
        snowballQuality = int(input())
        snowballValue = math.pow((snowballSnow / snowballTime), snowballQuality)
        if snowballValue > max_snowball_value:
            max_snowball_value = snowballValue
            max_snowball_snow = snowballSnow
            max_snowball_time = snowballTime
            max_snowball_quality = snowballQuality
        else:
            continue

    print(f'{max_snowball_snow} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})')