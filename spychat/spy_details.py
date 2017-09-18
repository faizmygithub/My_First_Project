from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Fiaz', 'Mr.', 4.9, 20)
friend_two = Spy('Harit', 'Mr.', 4.39, 20)
friend_three = Spy('Ayush', 'Mr.', 4.95, 20)


friends = [friend_one, friend_two, friend_three]


