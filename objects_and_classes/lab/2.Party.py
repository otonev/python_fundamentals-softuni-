#!/usr/bin/env python
class Party:
    def __init__(self):
        self.people = []

    def get_attendees(self, people):
        self.people = people
        return f"Going: {', '.join(self.people)}"

    def get_attendees_count(self, people):
        self.people = people
        return f"Total: {len(self.people)}"


party = Party()
command = input()
while command != "End":
    person = command
    party.people.append(person)
    command = input()

print(party.get_attendees(party.people))
print(party.get_attendees_count(party.people))