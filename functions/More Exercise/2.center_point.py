#!/usr/bin/env python

if __name__ == "__main__":
    import math
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())


    def calc_distance(x, y):
        distance = math.pow(x, 2) + math.pow(y, 2)
        return distance


    distance1 = calc_distance(x1, y1)
    distance2 = calc_distance(x2, y2)

    if distance1 <= distance2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")
