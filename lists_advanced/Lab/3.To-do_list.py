#!/usr/bin/env python
if __name__ == "__main__":
    command = input()
    tasks_with_priority = []
    while command != "End":
        tokens = command.split("-", maxsplit=1)
        priority = int(tokens[0])
        task = tokens[1]
        tasks_with_priority.append((priority, task))
        command = input()
    tasks = [task for priority, task in sorted(tasks_with_priority)]
    print(tasks)
