from datetime import datetime
class Spy:
  def __init__(self, Name, Salutation, Age, Rating):
    self.name = Name
    self.salutation=Salutation
    self.age = Age
    self.rating = Rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

spy=Spy('Aryan','Mr.',24,2.4)


class ChatMessage:
  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me