import uuid
class Resources:
    def __init__(self, url, text, report_id):
        self.uuid = uuid.uuid4()
        self.url = url
        self.text = text
        self.report_id = report_id



