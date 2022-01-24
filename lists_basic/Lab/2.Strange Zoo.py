#!/usr/bin/env python

if __name__ == "__main__":
    tail = input()
    body = input()
    head = input()
    meerkat = [tail,body,head]
    meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
    print(meerkat)