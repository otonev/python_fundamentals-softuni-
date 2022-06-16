#!/usr/bin/env python

if __name__ == "__main__":
    countries = input().split(", ")
    capitals = input().split(", ")
    result = dict(zip(countries, capitals))
    for country, capital in result.items():
        print(f"{country} -> {capital}")
