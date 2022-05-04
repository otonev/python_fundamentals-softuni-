#!/usr/bin/env python
if __name__ == "__main__":
    employee_stats = list(map(int, input().split()))
    improvement_factor = int(input())
    employee_stats = [employee_stat * improvement_factor for employee_stat in employee_stats]
    office_average = sum(employee_stats) / len(employee_stats)
    satisfied_employees = [employee_stat for employee_stat in employee_stats if employee_stat >= office_average]
    if 2 * len(satisfied_employees) < len(employee_stats):
        print(f"Score: {len(satisfied_employees)}/{len(employee_stats)}. Employees are not happy!")
    else:
        print(f"Score: {len(satisfied_employees)}/{len(employee_stats)}. Employees are happy!")