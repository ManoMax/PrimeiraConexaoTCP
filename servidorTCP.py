import socket

HOST = '150.165.42.166'
PORT = 8012

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    while True:
        msg = con.recv(1024)
        con.send(msg)
        if not msg: break
    con.close()
