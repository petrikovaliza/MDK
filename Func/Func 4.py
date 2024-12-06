#19.5

messages = ['Hi', 'Try again','Hello','Byebye']
def show_messages(messages):
    for message in messages:
        print(message)
        
show_messages(messages)

#19.6

def send_messages(messages, sent_messages):
    while message:
        current_message = messages.pop()
        print(f"{current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nОтправленные сообщения: ")
    for sent_message in sent_messages:
        print(sent_message)
    
message = ['Hi', 'Try again','Hello','Byebye']
sent_messages = []

send_messages(message, sent_messages)
show_sent_messages(sent_messages)

print(message)
print(sent_messages)

#19.7

send_messages( messages[:],sent_messages)