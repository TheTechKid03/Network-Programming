# Importing crucial libraries
import socket


# Variables for Later Use
Server_Ip = input("Enter The Target Socket IP Address you want to communicate with: ")
Port_number = input("Enter The Target Socket Port you want to communicate with: ")


# Socket Important Information
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((Server_Ip, int(Port_number)))

while True:

    # 1
    c, Client_address = s.recvfrom(4096)
    Text_from_client = c.decode()
    Upper_case = Text_from_client.upper()
    s.sendto(Upper_case.encode(), Client_address)

    # 2
    Send_This_Text_To_Client = "The quick brown fox jumps over the lazy dog"
    s.sendto(Send_This_Text_To_Client.encode(), Client_address)
    # s.close()
