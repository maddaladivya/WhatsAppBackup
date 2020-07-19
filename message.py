class Message:
    def __init__(self, timestamp, sent_by, text):
        self.timestamp = timestamp
        self.sent_by = sent_by
        self.text = text

    @staticmethod
    def get_timestamp_sentby_splitter():
        return "-"

    @staticmethod
    def get_sentby_text_splitter():
        return ":"

    def __str__(self):
        return f"{self.timestamp} {Message.get_timestamp_sentby_splitter()} {self.sent_by}" \
               f"{Message.get_sentby_text_splitter()} {self.text}"
