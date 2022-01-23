#!/usr/bin/env python

if __name__ == "__main__":
    lost_fights = int(input())
    helmet_price = float(input())
    sword_price = float(input())
    shield_price = float(input())
    armour_price = float(input())

    helmet_repairs = 0
    sword_repairs = 0
    shield_repairs = 0
    armour_repairs = 0

    for losses in range(1, lost_fights + 1):
        if losses % 3 == 0 and losses % 2 == 0:
            helmet_repairs += 1
            sword_repairs += 1
            shield_repairs += 1
            if shield_repairs % 2 == 0:
                armour_repairs += 1
        elif losses % 2 == 0:
            helmet_repairs += 1
        elif losses % 3 == 0:
            sword_repairs += 1

    expenses = (helmet_price * helmet_repairs) + (sword_price * sword_repairs) + (shield_price * shield_repairs) + (armour_price * armour_repairs)
    print(f'Gladiator expenses: {expenses:.2f} aureus')