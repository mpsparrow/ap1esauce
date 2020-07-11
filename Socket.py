import socket
from settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
	s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
	return s