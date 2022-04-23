#!/usr/bin/env python

if __name__ == "__main__":
    number_sequence = input().split()
    number_sequence = [int(i) for i in number_sequence]
    finish_line = len(number_sequence) // 2
    left_time = 0
    right_time = 0


    def calculate_time(index, racer):
        time = number_sequence[index]
        if time == 0:
            racer = racer * 0.8
        else:
            racer = racer + time
        return racer

    for i in range(0, finish_line):
        left_time = calculate_time(i, left_time)
    for i in range(len(number_sequence) - 1, finish_line, -1):
        right_time = calculate_time(i, right_time)

    if left_time < right_time:
        print(f"The winner is left with total time: {left_time:.1f}")
    else:
        print(f"The winner is right with total time: {right_time:.1f}")
