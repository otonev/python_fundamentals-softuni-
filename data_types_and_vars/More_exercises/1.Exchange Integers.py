#!/usr/bin/env python

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print("Before:")
    print(f"a = {a}")
    print(f"b = {b}")
    a, b = b, a
    print("After:")
    print(f"a = {a}")
    print(f"b = {b}")