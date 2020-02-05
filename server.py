import socket, json, xmltodict

# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1238))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    message = ("Hello Friend.")

    # JSON
    with open('a.json', 'r') as A:
        a = json.load(A)
    
    # XML
    with open('b.xml') as B:
        b = xmltodict.parse(B.read())

    print("----------------------------------------------------------------")
    print("[a] - JSON")
    print("[b] - XML")
    select = input("Select a protocol: ")
    print("----------------------------------------------------------------")
    
    if select == 'a':
        clientsocket.send(bytes(str(a),"utf-8"))
        clientsocket.close()
    if select == 'b':
        clientsocket.send(bytes(str(b),"utf-8"))
        clientsocket.close()

    