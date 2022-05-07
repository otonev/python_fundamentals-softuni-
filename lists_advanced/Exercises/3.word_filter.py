#!/usr/bin/env python
if __name__ == "__main__":
    text = input().split()
    filtered = [word for word in text if len(word) % 2 == 0]
    print("\n".join(filtered))
