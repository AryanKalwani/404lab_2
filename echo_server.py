import socket
import time
import threading

host = ""
port = 8001
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(2)

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=threadss, args=(conn, addr))

def threadss(conn,addr):
    #print(conn, addr)
    full_data = conn.recv(buffer_size)
    time.sleep(0.5)
    print(full_data)
    conn.sendall(full_data)
    conn.close()