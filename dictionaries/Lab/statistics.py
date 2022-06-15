#!/usr/bin/env python
if __name__ == "__main__":
    command = input()
    products = {}
    while command != "statistics":
        tokens = command.split(": ")
        product = tokens[0]
        quantity = tokens[1]
        if product not in products:
            products[product] = 0
        products[product] += int(quantity)
        command = input()
    print("Products in stock:")
    for product, quantity in products.items():
        print(f"- {product}: {quantity}")
    print(f"Total Products: {len(products.keys())}")
    print(f"Total Quantity: {sum(products.values())}")