import socket, json, time, os
from _thread import *
from datetime import datetime

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        data = json.loads(data.decode())
        data["last_update"] = time.time()
        with open(f"""{os.path.abspath(os.path.dirname(__file__))}/json/workers/{data["stratum"]["user"].split(".")[-1]}.json""","w",) as outfile:
            json.dump(data, outfile, indent=2)
        print(f"""> Received from {data["stratum"]["user"].split(".")[-1]}: {datetime.now()}""")
    c.close()

if __name__ == "__main__":
    HOST = ""
    PORT = 25564
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)  
    while True:
        c, addr = s.accept()
        start_new_thread(threaded, (c,))