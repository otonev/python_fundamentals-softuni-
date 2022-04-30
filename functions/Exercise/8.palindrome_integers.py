#!/usr/bin/env python

if __name__ == "__main__":
    def palindrome_check(numbers):
        for num in numbers:
            num = int(num)
            temp = num
            reversed = 0
            while num > 0:
                dig = num % 10
                reversed = reversed * 10 + dig
                num = num // 10
            if temp == reversed:
                is_palindrome = True
            else:
                is_palindrome = False
            print(is_palindrome)

    nums = input().split(', ')
    palindrome_check(nums)
