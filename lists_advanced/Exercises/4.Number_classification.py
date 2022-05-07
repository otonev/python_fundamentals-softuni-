#!/usr/bin/env python
if __name__ == "__main__":
    numbers = list(map(int, input().split(", ")))
    positive = [str(num) for num in numbers if num >= 0]
    negative = [str(num) for num in numbers if num < 0]
    even = [str(num) for num in numbers if num % 2 == 0]
    odd = [str(num) for num in numbers if num %2 != 0]
    print(f"Positive: "+", ".join(positive) +
          "\n"+"Negative: "+", ".join(negative) +
          "\n"+"Even: "+", ".join(even) +
          "\n"+"Odd: "+", ".join(odd)+"\n")
