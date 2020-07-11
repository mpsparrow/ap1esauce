import string
import socket
from read import getUser, getMessage
from actions import chat, ban, timeout
from settings import HOST, PORT, PASS, IDENT, CHANNEL

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(IDENT).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHANNEL).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")

    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        try:
            user = getUser(response)
            message = getMessage(response)
            if "hi" in message.lower():
                chat(s, "hello")
        except:
            print("issue")
        print(response)
