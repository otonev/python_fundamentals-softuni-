#!/usr/bin/env python

if __name__ == "__main__":
    n = int(input())
    registered_vehicles = {}

    def register_vehicle(user, plate_number, vehicles_dict):
        if user in vehicles_dict:
            print(f"ERROR: already registered with plate number {vehicles_dict[user]}")
        else:
            vehicles_dict[user] = plate_number
            print(f"{user} registered {plate_number} successfully")

    def unregister_vehicle(user, vehicles_dict):
        if user not in vehicles_dict:
            print(f"ERROR: user {user} not found")
        else:
            vehicles_dict.pop(user)
            print(f"{user} unregistered successfully")

    def print_vehicles(vehicles_dict):
        for k, v in vehicles_dict.items():
            print(f"{k} => {v}")

    for i in range(n):
        command = input().split()
        action = command[0]
        username = command[1]
        if action == 'register':
            license_plate = command[2]
            register_vehicle(username, license_plate, registered_vehicles)
        elif action == 'unregister':
            unregister_vehicle(username, registered_vehicles)

    print_vehicles(registered_vehicles)
