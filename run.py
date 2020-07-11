import string
from read import getUser, getMessage
from socket import openSocket, sendMessage
from Initialize import joinRoom
from settings import RATE

s = openSocket()

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)
		username = re.search(r"\w+", line).group(0) # return the entire match
        message = CHAT_MSG.sub("", line)
        print(username + ": " + message)
	
	sleep(1 / RATE)
