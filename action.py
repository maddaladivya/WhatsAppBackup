class Action:

    def __init__(self, timestamp, action_message):
        self.timestamp = timestamp
        self.action_message = action_message

    def __str__(self):
        return self.timestamp + " - " + self.action_message

    @staticmethod
    def get_timestamp_sentby_splitter():
        return "-"
