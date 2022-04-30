#/usr/bin/env python

if __name__ == "__main__":
    def print_trib_number_recursive(n):
        if n == 1 or n == 2:
            trib_n = 1
            return trib_n
        elif n == 3:
            trib_n = 2
            return trib_n
        else:
            trib_n = print_trib_number_recursive(n - 1) + \
                     print_trib_number_recursive(n - 2) + \
                     print_trib_number_recursive(n - 3)
            return trib_n


    def print_trib(n):
        for i in range(1, n + 1):
            print(print_trib_number_recursive(i), end=" ")


    n = int(input())
    print_trib(n)
