import yc_message

yc_message.send_message.send("hello")
text = yc_message.receive_message.receive()
print(text)
