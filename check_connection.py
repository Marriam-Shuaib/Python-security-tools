import socket

def check_connection(hostname, port):
    try:
        socket.create_connection((hostname, port))
        print("Connected to " + hostname + " on port " + str(port))
    except:
        print("Connection failed to " + hostname)

hostname = input("Enter hostname: ")
port = int(input("Enter port: "))
check_connection(hostname, port)