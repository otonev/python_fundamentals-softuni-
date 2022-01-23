#!/usr/bin/env python
import math

if __name__ == "__main__":
    party_size = int(input())
    days = int(input())
    companions = party_size
    gold_coins_total = 0
    spent_coins = 0

    for day in range(1, days + 1):
        gold_coins_day = 50
        price_water = 0
        price_food = 2
        price_extra = 0

        if day % 10 == 0 and day % 15 == 0:
            companions -= 2
            companions += 5
        elif day % 10 == 0:
            companions -= 2
        elif day % 15 == 0:
            companions += 5

        if day % 5 == 0 and day % 3 == 0:
            gold_coins_day = gold_coins_day + (20 * companions)
            price_water = 3
            price_extra = 2
        elif day % 3 == 0:
            price_water = 3
        elif day % 5 == 0:
            gold_coins_day = gold_coins_day + (20 * companions)

        spent_coins_day = (price_food + price_water + price_extra) * companions
        gold_gained_day = gold_coins_day - spent_coins_day
        gold_coins_total += gold_gained_day
        spent_coins += spent_coins_day

    coins_per_comp = math.floor(gold_coins_total / companions)
    print(f"{companions} companions received {coins_per_comp} coins each.")
    