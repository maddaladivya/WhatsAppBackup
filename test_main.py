from parser import ChatParser
if __name__ == "__main__":
    chat_file_location = "after date change.txt"
    chat_parser = ChatParser()
    chat_parser.parse(open(chat_file_location, "r", encoding="utf8"))
