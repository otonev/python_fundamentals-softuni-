#!/usr/bin/env python
if __name__ == "__main__":
    n = int(input())
    train = [0 for _ in range(n)]
    command = input()
    while command != "End":
        tokens = command.split()
        command = tokens[0]
        if command == "add":
            people_to_add = int(tokens[1])
            train[-1] += people_to_add
        elif command == "insert":
            wagon_to_insert = int(tokens[1])
            people_to_insert = int(tokens[2])
            train[wagon_to_insert] += people_to_insert
        elif command == "leave":
            wagon_to_remove = int(tokens[1])
            people_to_remove = int(tokens[2])
            train[wagon_to_remove] -= people_to_remove
        command = input()
    print(train)
