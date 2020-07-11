import string
from read import getUser, getMessage
from socket import openSocket
from actions import chat, ban, timeout
from settings import RATE

s = openSocket()

while True:
    response = s.recv(1024).decode("utf-8")

    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)

    sleep(1 / RATE)
