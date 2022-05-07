#!/usr/bin/env python
if __name__ == "__main__":
    total_electrons = int(input())

    result = []
    shield_index = 1
    while total_electrons > 0:
        value = 2 * shield_index ** 2
        if total_electrons >= value:
            result.append(value)
            shield_index += 1
            total_electrons -= value
        else:
            result.append(total_electrons)
            total_electrons = 0

    print(result)