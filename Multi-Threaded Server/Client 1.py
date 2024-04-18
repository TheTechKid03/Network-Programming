def Client1():

    # Importing crucial libraries
    import socket

    IP = 'localhost'
    Port = 45826
    Host = (IP, Port)


    # Socket Important Information/Connection
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(Host)


    # 3
    Prompt_1 = c.recv(1024).decode()
    print(Prompt_1)
    Number_1 = input(" ").encode()
    c.send(Number_1)
    Prompt_2 = c.recv(1024).decode()
    print(Prompt_2)
    Number_2 = input(" ").encode()
    c.send(Number_2)
    Answer = c.recv(1024).decode()
    print(Answer)
    c.close()
