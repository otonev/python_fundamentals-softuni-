#!/usr/bin/env python

if __name__ == "__main__":
    GBP_TO_USD_RATE = 1.31
    pounds = float(input())
    dollars = pounds * GBP_TO_USD_RATE
    print(f'{dollars:.3f}')