#!/usr/bin/env python

if __name__ == "__main__":
    import math
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())

    def calc_distance_to_center(x, y):
        distance = math.pow(x, 2) + math.pow(y, 2)
        return distance


    def calc_line_length(x1, y1, x2, y2):
        line_length = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        return line_length


    line1_length = calc_line_length(x1, y1, x2, y2)
    line2_length = calc_line_length(x3, y3, x4, y4)

    if line1_length >= line2_length:
        distance1 = calc_distance_to_center(x1, y1)
        distance2 = calc_distance_to_center(x2, y2)
        if distance1 <= distance2:
            print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
        else:
            print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
    else:
        distance1 = calc_distance_to_center(x3, y3)
        distance2 = calc_distance_to_center(x4, y4)
        if distance1 <= distance2:
            print(f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})")
        else:
            print(f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})")
