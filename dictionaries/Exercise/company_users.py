#!/usr/bin/env python

if __name__ == "__main__":
    companies = {}
    command = input()

    def add_user_to_company(uid, company, companies_dict):
        if company not in companies_dict:
            companies_dict[company] = []
        if uid not in companies_dict[company]:
            companies_dict[company] += [uid]

    def print_companies(companies_dict):
        for company, users in companies_dict.items():
            print(company)
            for user in users:
                print(f"-- {user}")


    while command != "End":
        tokens = command.split(" -> ")
        company = tokens[0]
        uid = tokens[1]
        add_user_to_company(uid, company, companies)
        command = input()

    print_companies(companies)
