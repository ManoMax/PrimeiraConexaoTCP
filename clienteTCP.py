# coding: utf-8
import socket

# Terminal HOST: ifconfig
# PORT aleatoria acima de 1024
HOST = 'localhost'
PORT = 8012

# Atribuindo uma Conexao TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

# Lendo entrada do cliente
msg = input()

#Enquanto for != 'bye' retorna a própria entrada
while msg != 'bye':
    # Enviando mensagem ao Servidor
    tcp.send (msg)
    # Com padrão de 1024 bits por envio.
    saida = tcp.recv(1024)
    print (saida)
    msg = raw_input()
tcp.close()
