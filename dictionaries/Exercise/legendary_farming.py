#!/usr/bin/env python

if __name__ == "__main__":
    def append_dict(key, dictionary, value=0):
        if key not in dictionary:
            dictionary[key] = value
        else:
            dictionary[key] += value
    
    def print_dictionary(dict):
        for k, v in dict.items():
            print(f"{k}: {v}")

    key_materials = {
        "shards": 0,
        "fragments":0,
        "motes": 0
    }
    legendary_items = {
        "shards": "Shadowmourne",
        "fragments": "Valanyr",
        "motes": "Dragonwrath"
    }
    junk = {}
    game_over = False
    while not game_over:
        command = input().split()
        for i in range(0, len(command), 2):
            quantity = int(command[i])
            material = command[i+1].lower()
            if material != "shards" and material != 'fragments' and material != 'motes':
                append_dict(material, junk, quantity)
            else:
                key_materials[material] += quantity
                if key_materials[material] >= 250:
                    print(f"{legendary_items[material]} obtained!")
                    key_materials[material] -= 250
                    game_over = True
                    break
    print_dictionary(key_materials)
    print_dictionary(junk)
