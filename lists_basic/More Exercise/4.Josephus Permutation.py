#!/usr/bin/env python

if __name__ == "__main__":
    number_sequence = input().split()
    number_sequence = [int(i) for i in number_sequence]
    killed_order = []
    k = int(input())
    counter = 0
    index = 0
    while len(number_sequence) > 0:
        counter += 1

        if counter % k == 0:
            killed_order.append(number_sequence.pop(index))
        else:
            index += 1

        if index >= len(number_sequence):
            index = 0

    print(str(killed_order).replace(' ', '').replace('\'', ''))
