#!/usr/bin/env python
if __name__ == "__main__":
    def read_products():
        items = input().split()
        products = {}
        for i in range(0, len(items), 2):
            product = items[i]
            quantity = items[i + 1]
            products[product] = int(quantity)
        return products

    print(read_products())
