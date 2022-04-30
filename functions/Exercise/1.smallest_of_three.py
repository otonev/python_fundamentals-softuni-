#!/usr/bin/env python

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    
    def smallest_of_three_nums(x, y, z):
        if x <= y and x <= z:
            return x
        if y <= x and y <= z:
            return y
        if z <= x and z <= y:
            return z


    print(smallest_of_three_nums(num1, num2, num3))
