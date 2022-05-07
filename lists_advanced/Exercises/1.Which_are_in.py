#!/usr/bin/env python
if __name__ == "__main__":
    words = input().split(", ")
    text = input()

    result = [word for word in words if word in text]
    print(result)