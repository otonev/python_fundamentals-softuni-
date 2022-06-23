#!/usr/bin/env python
if __name__ == "__main__":
    def add_challenger(name, role, skill, collection):
        if name not in collection:
            collection[name] = {}
        if role not in collection[name]:
            collection[name][role] = skill
        else:
            if skill > collection[name][role]:
                collection[name][role] = skill

    def duel(challenger_one, challenger_two, collection):
        c1_roles = collection[str(challenger_one)].keys()
        c2_roles = collection[str(challenger_two)].keys()
        for role in c1_roles:
            if role in c2_roles:
                c1_skill_pts = collection[challenger_one][role]
                c2_skill_pts = collection[challenger_two][role]
                if c1_skill_pts > c2_skill_pts:
                    collection.pop(challenger_two)
                    return True
                elif c1_skill_pts < c2_skill_pts:
                    collection.pop(challenger_one)
                    return True

    challengers = {}
    command = input()
    while command != "Season end":
        command = command.split(" -> ")
        if len(command) < 3:
            command = ''.join(e for e in command)
            command = command.split(" vs ")
            challenger1 = command[0]
            challenger2 = command[1]
            if challenger1 not in challengers or challenger2 not in challengers:
                command = input()
                continue
            is_popped = duel(challenger1, challenger2, challengers)
            if is_popped:
                command = input()
                continue
            command = input()
        else:
            challenger_name = command[0]
            challenger_role = command[1]
            challenger_skill_pts = int(command[2])
            add_challenger(challenger_name, challenger_role, challenger_skill_pts, challengers)
            command = input()

    challengers_skills = {k: sum(v.values())for k, v in challengers.items()}
    challengers_skills = dict(sorted(challengers_skills.items(), key=lambda x: (-x[1], x[0])))
    for name, skill_total in challengers_skills.items():
        print(f"{name}: {skill_total} skill")
        roles = dict(sorted(challengers[name].items(), key=lambda x: (-x[1], x[0])))
        for role, skill in roles.items():
            print(f"- {role} <::> {skill}")
