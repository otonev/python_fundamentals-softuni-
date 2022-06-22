#!/usr/bin/env python

if __name__ == "__main__":
    statistics = {}
    contests = {}

    def add_to_stats(user, score, stats):
        if user not in stats:
            stats[user] = score
        else:
            stats[user] += score

    def add_to_contests(user, contest, score, collection):
        if contest not in collection:
            collection[contest] = {}
        if user not in collection[contest]:
            collection[contest][user] = score
        else:
            if collection[contest][user] < score:
                collection[contest][user] = score

    def print_contest(collection):
        for contest in collection.keys():
            print(f"{contest}: {len(collection[contest])} participants")
            counter = 1
            for k, v in sorted(collection[contest].items(), key=lambda x: (-x[1], x[0])):
                print(f"{counter}. {k} <::> {v}")
                counter += 1

    def print_stats(collection):
        counter = 1
        print("Individual standings:")
        for k, v in sorted(collection.items(), key=lambda x: (-x[1], x[0])):
            print(f"{counter}. {k} -> {v}")
            counter += 1

    command = input()
    while command != "no more time":
        student_name, contest_name, result = command.split(" -> ")
        score_changed = False
        result = int(result)
        add_to_contests(student_name, contest_name, result, contests)
        command = input()

    for key in contests.keys():
        for user, score in contests[key].items():
            add_to_stats(user, score, statistics)

    print_contest(contests)
    print_stats(statistics)
