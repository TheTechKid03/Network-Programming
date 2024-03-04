# Importing crucial libraries
import socket


# Variables for Later Use
Server_Ip = input("Enter The Socket IP Address you want to assign: ")
Port_number = input("Enter The Socket Port you want to assign: ")


# Socket Important Information
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((str(Server_Ip), int(Port_number)))
s.listen()

while True:
    c, Client_address = s.accept()

    # 1
    Receive_Client_Greeting = c.recv(1024).decode()
    if Receive_Client_Greeting == "Hello":
        print(Receive_Client_Greeting)
        Send_Client_Greeting = input("Send a Greeting Message Back to The Client: \n").encode()
        c.send(Send_Client_Greeting)

    # 2
    Client_Name = c.recv(512).decode()
    print("The name of the Client Connected is: ", Client_Name)

    # 3
    Prompt_1 = "Enter Any Number You Wish to Add: ".encode()
    c.send(Prompt_1)
    Prompt_2 = "Enter Any Number Again to get the Addition between the two: ".encode()
    c.send(Prompt_2)
    Receive_Client_Number_1 = c.recv(1024).decode()
    Receive_Client_Number_2 = c.recv(1024).decode()
    Arithmetic_Operation = int(Receive_Client_Number_1) + int(Receive_Client_Number_2)
    Answer = ("The Answer of the Specified Arithemetic Operation is: " + str(Arithmetic_Operation)).encode()
    c.send(Answer)
    c.close()
