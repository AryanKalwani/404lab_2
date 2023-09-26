import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080
payload = f'GET / HTTP/1.0\r\nHost: {"www.google.com"}\r\n\r\n'
buffer_size = 4096

remote_ip = socket.gethostbyname(host)

s.connect((remote_ip, port))

s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR)

full_data = b''
while True:
    data = s.recv(buffer_size)
    if not data:
        break
    full_data += data
print(full_data)
s.close()
