import datetime

from action import Action
from message import Message


class ChatParser:
    def __init__(self, timestamp_format="%d/%m/%y, %I:%M %p"):
        self.timestamp_format = timestamp_format

    def is_timestamp(self, text):
        try:
            datetime.datetime.strptime(text, self.timestamp_format)
            return True
        except ValueError:
            return False

    def split_raw_message_data(self, raw_message_data):
        timestamp_sentby_splitter = Message.get_timestamp_sentby_splitter()
        sentby_text_splitter = Message.get_sentby_text_splitter()
        timestamp, other_data = raw_message_data.split(timestamp_sentby_splitter, 1)
        sent_by, message_text = other_data.split(sentby_text_splitter, 1)
        return timestamp, sent_by, message_text

    def split_raw_action_data(self, raw_action_data):
        return raw_action_data.split(Action.get_timestamp_sentby_splitter(), 1)

    def contains_message_header(self, text):
        if Message.get_timestamp_sentby_splitter() in text:
            possible_timestamp, other_data = text.split(Message.get_timestamp_sentby_splitter(), 1)
            if self.is_timestamp(possible_timestamp.strip()) and Message.get_sentby_text_splitter() in other_data:
                return True
        return False

    def contains_action_header(self, text):
        if Action.get_timestamp_sentby_splitter() in text:
            possible_timestamp = text.split(Action.get_timestamp_sentby_splitter(), 1)[0].strip()
            if self.is_timestamp(possible_timestamp):
                return True
        return False

    def parse(self, chat_file):
        data_buffer = []
        message_start = False
        action_start = False
        chat = []
        raw_chat_data = []
        for line in chat_file:
            if self.contains_message_header(line) or self.contains_action_header(line):
                if len(data_buffer) != 0:
                    if message_start:
                        raw_chat_data.append(("Message", '\n'.join(data_buffer)))
                        message_start = False
                    if action_start:
                        raw_chat_data.append(("Action", '\n'.join(data_buffer)))
                        action_start = False
                    data_buffer = []
                if self.contains_message_header(line):
                    message_start = True
                elif self.contains_action_header(line):
                    action_start = True
            data_buffer.append(line)
        for item in raw_chat_data:
            item_type = item[0]
            raw_data = item[1]
            if item_type == "Message":
                timestamp, sent_by, message_text = self.split_raw_message_data(raw_data)
                message = Message(timestamp, sent_by, message_text)
                chat.append(message)
            elif item_type == "Action":
                timestamp, action_message = self.split_raw_action_data(raw_data)
                chat.append(Action(timestamp, action_message))

        for chat_item in chat:
            if type(chat_item) == Action:
                print(chat_item)


