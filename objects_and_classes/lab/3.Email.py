#!/usr/bin/env python
class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


class MailBox:
    def __init__(self):
        self.emails = []


mailbox = MailBox()
while True:
    command = input()
    if command == "Stop":
        break
    else:
        sender, receiver, content = command.split()
        email = Email(sender, receiver, content)
        mailbox.emails.append(email)

indexes_to_send = list(map(int, input().split(", ")))
for index in indexes_to_send:
    Email.send(mailbox.emails[index])

for email in mailbox.emails:
    print(email.get_info())
