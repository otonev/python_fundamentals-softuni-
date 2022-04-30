#!/usr/bin/env python

if __name__ == "__main__":
    def parse(string, user_input):
        if string == "int":
            user_input = int(user_input) * 2
            return f"{user_input}"
        elif string == "real":
            user_input = float(user_input) * 1.5
            return f"{user_input:.2f}"
        elif string == "string":
            return f"${user_input}$"


    data_type = input()
    value = input()
    print(parse(data_type, value))
