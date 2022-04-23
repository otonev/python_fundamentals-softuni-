#!/usr/bin/env python

if __name__ == "__main__":
    def calculate_order(item: str, count: int):
        price = 0
        if item == "coffee":
            price = 1.5
        elif item == "water":
            price = 1.0
        elif item == "coke":
            price = 1.4
        elif item == "snacks":
            price = 2.0
        return price * count


    ordered_item = input()
    quantity = int(input())
    print(f"{calculate_order(ordered_item, quantity):.2f}")
