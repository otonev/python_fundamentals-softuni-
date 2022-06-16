#!/usr/bin/env python

if __name__ == "__main__":
    phonebook = {}
    while True:
        command = input().split("-")
        if len(command) < 2:
            break
        else:
            name = command[0]
            phone = command[1]
            phonebook[name] = phone
    contacts_count = int(command.pop())
    for _ in range(0, contacts_count):
        name = input()
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"Contact {name} does not exist.")
