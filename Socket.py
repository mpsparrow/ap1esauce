import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send(f"{PASS} " + f"{PASS}" + "\r\n")
	s.send(f"{NICK} " + f"{IDENT}" + "\r\n")
	s.send(f"{JOIN} #" + f" {CHANNEL}" + "\r\n")
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)
