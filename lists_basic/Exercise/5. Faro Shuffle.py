#!/usr/bin/env python

if __name__ == "__main__":
    deck = input().split()
    shuffles = int(input())

    def shuffle(deck):
        half_deck = len(deck) // 2
        res = []
        for i in range(half_deck):
            index_sec_card = i + half_deck
            first_card = deck[i]
            sec_card = deck[index_sec_card]
            res.append(first_card)
            res.append(sec_card)
        return res

    def main(deck, shuffles):
        for i in range(shuffles):
            deck = shuffle(deck)
        return deck

    deck = main(deck, shuffles)
    print(deck)
