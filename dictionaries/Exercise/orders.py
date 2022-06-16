#!/usr/bin/env python

if __name__ == "__main__":
    def add_product_to_cart(cart, product, quantity, price):
        if product in cart:
            cart[product]['quantity'] += float(quantity)
            cart[product]['price'] = float(price)
        else:
            cart[product] = {'quantity': 0, 'price': 0}
            cart[product]['quantity'] = float(quantity)
            cart[product]['price'] = float(price)

    def print_cart(cart):
        for k, v in cart.items():
            total_price = v['quantity'] * v['price']
            print(f"{k} -> {total_price:.2f}")

    command = input()
    shopping_cart = {}
    while command != "buy":
        tokens = command.split()
        name = tokens[0]
        price = tokens[1]
        quantity = tokens[2]
        add_product_to_cart(shopping_cart, name, quantity, price)
        command = input()
    print_cart(shopping_cart)
