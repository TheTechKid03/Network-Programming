# Importing crucial libraries
import socket


# Variables for Later Use
Server_Ip = input("Enter The Target Socket IP Address you want to communicate with: ")
Port_number = input("Enter The Target Socket Port you want to communicate with: ")


# Socket Important Information/Connection
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 1
Greeting_Message = input("Enter a word in lowercase: \n").encode()
c.sendto(Greeting_Message, (str(Server_Ip), int(Port_number)))
Text_from_server = c.recvfrom(4096)
print(Text_from_server)

# 2
Receive_This_From_Server = c.recvfrom(8192)
print(Receive_This_From_Server)
c.close()
