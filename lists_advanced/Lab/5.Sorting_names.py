#!/usr/bin/env python
if __name__ == "__main__":
    names = input().split(", ")
    print(sorted(names, key=lambda x: (-len(x), x)))
    