#!/usr/bin/env python

if __name__ == "__main__":
    pos = list()
    neg = list()
    n = int(input())
    for _ in range(n):
        current_num = int(input())
        if current_num >= 0:
            pos.append(current_num)
        else:
            neg.append(current_num)
    print(pos)
    print(neg)
    print(f"Count of positives: {len(pos)}")
    print(f"Sum of negatives: {sum(neg)}")
