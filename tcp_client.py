import socket

target_host = 'www.google.com'
target_port = 80

# Create a scoket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET means we're going to be using the standard IPv4 address
                                                            # SOCK_STTREAM means this will be a TCP client

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print response