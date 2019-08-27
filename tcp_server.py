import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))   # IP and port number to listen on

server.listen(5)    # Maximum backlog of connections set to 5

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# this is our client-handing thread
def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)

    print "[*] Received %s" % request

    # send back a packet
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client, addr = server.accept()  # when a client connects client will contain client socket, and addr  will contain the remote connection details.
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])

    # spin up our client thread to handle incming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()