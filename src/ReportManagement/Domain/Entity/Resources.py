import uuid
class Resources:
    def __init__(self, title, descrip):
        self.uuid = uuid.uuid4()
        self.title = title
        self.descrip = descrip



