#!/usr/bin/env python

if __name__ == "__main__":
    def return_rect_area(w: int, h: int):
        return w*h

    width = int(input())
    height = int(input())
    print(return_rect_area(width, height))
