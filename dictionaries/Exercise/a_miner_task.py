#!/usr/bin/env python

if __name__ == "__main__":
    resources = {}
    count = 1
    command = input()
    while command != "stop":
        resource = command
        quantity = int(input())
        if resource in resources:
            resources[resource] += quantity
        else:
            resources[resource] = quantity
        command = input()

    for k, v in resources.items():
        print(f"{k} -> {v}")
