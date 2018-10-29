import socket

# Terminal HOST: ifconfig
# PORT aleatória acima de 1024
HOST = '150.165.42.166'
PORT = 8012

# Atribuindo uma Conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Em caso de fechamento inesperado, a Conexao é fechada
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Atribuindo uma Conexao TCP
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
	# Estabelecendo "ID" de uma Conexao TCP/Cliente (con)
    con, cliente = tcp.accept()

    # Recebendo mensagem do cliente, e retornando a mesma para ele
    while True:
        msg = con.recv(1024)
        con.send(msg)
        if not msg: break
    con.close()
