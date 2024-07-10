import uuid
class Downloadable:
    def __init__(self, url):
        self.uuid = uuid.uuid4()
        self.url = url
