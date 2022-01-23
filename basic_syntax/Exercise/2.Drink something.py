#!/usr/bin/env python

if __name__ == "__main__":
    age=int(input())
    if age <= 14:
        print("drink toddy")
    elif 14 < age <= 18:
        print("drink coke")
    elif 19 < age <= 21:
        print("drink beer")
    else:
        print("drink whisky")
