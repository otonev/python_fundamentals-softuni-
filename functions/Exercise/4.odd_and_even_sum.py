#!/usr/bin/env python

if __name__ == "__main__":
    num = int(input())
    num_copy = num


    def odd_even_sum(number, number_copy):
        if number == 0:
            print('Odd sum = 0, Even sum = 0')
            exit()
        while number > 0:
            current_num = number % 10
            if number == num_copy:
                odd_sum = 0
                even_sum = 0
            if current_num % 2 == 0:
                even_sum += current_num
            else:
                odd_sum += current_num
            number = number // 10
        print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


    odd_even_sum(num, num_copy)
