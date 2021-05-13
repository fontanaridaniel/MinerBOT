import socket, requests
from datetime import datetime

def connectToServer(host, port):
    try:
        s.connect((host, port))
        print(f"> Connected to the server.")
        return True
    except:
        print(f"> Can't connect to the server.")
        return False

def sendDataToSever():
    url = "http://localhost:22333/api/v1/status"
    try:
        response = requests.get(url)
    except:
        print("> Can't connect to miner API. Is it on?")
        return False
    try:
        s.send(response.content)
        print(f"> Sended: {datetime.now()}")
        return True
    except:
        pass
    print("> Can't send data to the server.")
    return False

if __name__ == "__main__":
    HOST = "fontanaridanielrasp.duckdns.org"
    PORT = 25564
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if connectToServer(host=HOST,port=PORT):
            while True:
                if not sendDataToSever():
                    break