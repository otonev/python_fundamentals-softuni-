#!/usr/bin/env python

if __name__ == "__main__":
    def perform_operation(a, b, operation):
        if operation == "add":
            return a + b
        if operation == 'subtract':
            return a - b
        if operation == 'divide':
            return int(a / b)
        if operation == 'multiply':
            return a * b


    op_string = input()
    num1 = int(input())
    num2 = int(input())
    print(perform_operation(num1, num2, op_string))
