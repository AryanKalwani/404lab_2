import socket
import threading
import time

host = ""
port = 8080
buffer_size = 4096

def threadss(conn, addr):
    full_data = conn.recv(buffer_size)
    time.sleep(0.5)
    #print(full_data)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host2 = 'www.google.com'
    port2 = 80
    remote_ip = socket.gethostbyname(host2)
    s2.connect((remote_ip, port2))

    s2.send(full_data)
    s2.shutdown(socket.SHUT_WR)

    full_data2 = b""
    while True:
        data = s2.recv(buffer_size)
        if not data:
            break
        full_data2 += data

    conn.sendall(full_data2)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(2)

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=threadss, args=(conn,addr))
        thread.run()
        
