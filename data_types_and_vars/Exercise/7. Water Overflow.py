#!/usr/bin/env python

if __name__ == "__main__":
    TANK_CAPACITY = 255
    n = int(input())
    liters_in_tank = 0
    for pours in range(0, n):
        current_liters = int(input())
        if current_liters + liters_in_tank > TANK_CAPACITY:
            print("Insufficient capacity!")
        else:
            liters_in_tank += current_liters

    print(liters_in_tank)