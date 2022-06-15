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

    def search_product(product):
        if product in products:
            quantity = products[product]
            return f"We have {quantity} of {product} left"
        return f"Sorry, we don't have {product}"

    products = read_products()
    searched_products = input().split()
    for product in searched_products:
        print(search_product(product))
