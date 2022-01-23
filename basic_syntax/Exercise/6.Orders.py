#!/usr/bin/env python

if __name__ == "__main__":
    total_sum = 0
    orders_num=int(input())
    for order in range(orders_num):
        price_per_capsule=float(input())
        days=int(input())
        capsules=int(input())
        price = price_per_capsule * days * capsules
        total_sum += price
        print(f"The price for the coffee is: ${price:.2f}")
    print(f"Total: ${total_sum:.2f}")
