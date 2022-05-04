#!/usr/bin/env python
if __name__ == "__main__":
    def is_palindrome(string):
        if string == string[::-1]:
            return True
        else:
            return False

    words = input().split()
    searched_palindrome = input()
    palindromes = [word for word in words if is_palindrome(word)]
    print(palindromes)
    searched_palindrome_count = len([palindrome for palindrome in palindromes if palindrome == searched_palindrome])
    print(f"Found palindrome {searched_palindrome_count} times")
