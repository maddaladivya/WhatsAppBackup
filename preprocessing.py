import datetime
def is_date(date):
    try:
        datetime.datetime.strptime(date, '%d/%m/%y')
        return True
    except ValueError:
        return False

chat_file = open(r'C:\Users\madda\Downloads\chat.txt', 'r', encoding="utf8")
date = []
time = []
name = []
msg = []

for message in chat_file:
    data = message.split(" ", 4)
    if(is_date(data[0][:-1])):
        date.append(data[0][:-1])
        time.append(data[1] + data[2])
        name_msg = data[4].split(":", 1)
        if(len(name_msg) == 2):
            name.append(name_msg[0])
            msg.append(name_msg[1])
        else:
            name.append("")
            msg.append(name_msg[0])
    else:
        if len(msg):
            msg[len(msg)-1] = msg[len(msg)-1] + "\n" + message
            
