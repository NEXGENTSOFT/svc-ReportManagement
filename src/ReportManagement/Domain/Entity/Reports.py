import uuid
class Report(object):
    def __init__(self, title, text, user_id, type):
        self.uuid = uuid.uuid4()
        self.title = title
        self.text = text
        self.user_id = user_id
        self.type = type

