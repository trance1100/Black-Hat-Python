import socket

target_host = '127.0.0.1'
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET means we're going to be using the standard IPv4 address
                                                           # Changed SOCK_DGRAM forUDP

# send some data - UDP is a connectionless protocol so we just send in the data
client.sendto("AAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print data