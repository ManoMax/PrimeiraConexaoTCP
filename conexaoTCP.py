import socket

HOST = '150.165.42.166'
PORT = 8012

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

msg = raw_input()
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()