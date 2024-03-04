# Importing crucial libraries
import socket


# Variables for Later Use
Server_Ip = input("Enter The Socket IP Address you want to assign: ")
Port_number = input("Enter The Socket Port you want to assign: ")


# Socket Important Information/Connection
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((str(Server_Ip), int(Port_number)))

# 1
Greeting_Message = input("Say Hello! to the sever to let it know connection has been established: \n").encode()
c.send(Greeting_Message)
Server_Greeting = c.recv(1024).decode()
print(Server_Greeting)

# 2
Name = input("What is Your Name?: \n").encode()
c.send(Name)

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
