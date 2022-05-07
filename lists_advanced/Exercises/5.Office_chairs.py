#!/usr/bin/env python
if __name__ == "__main__":
    n = int(input())
    free_chairs = 0
    is_printed = False
    for room in range(1, n +1):
        tokens = input().split()
        chairs = tokens[0]
        visitors = int(tokens[1])
        if len(chairs) >= visitors:
            free_chairs = free_chairs + (len(chairs) - visitors)
        else:
            print(f"{visitors - len(chairs)} more chairs needed in room {room}")
            is_printed = True
    if not is_printed:
        print(f"Game On, {free_chairs} free chairs left")
