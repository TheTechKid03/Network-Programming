# Importing crucial libraries
import socket


# Variables for Later Use
Server_Ip = input("Enter The Socket IP Address you want to assign: ")
Port_number = input("Enter The Socket Port you want to assign: ")

N = 0
Array_of_numbers = []

# Socket Important Information/Connection
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((str(Server_Ip), int(Port_number)))

Menu = c.recv(8192).decode()
print(Menu)
Option = input(" Which option do you select?: ").encode()
c.send(Option)

while True:
    if int(Option) == 1:
        Option_1_Condition_Breaker = input("Enter the size of your array: ").encode()
        c.send(Option_1_Condition_Breaker)

        while N < int(Option_1_Condition_Breaker):
            Number = input("Enter a number: ")
            Array_of_numbers = Array_of_numbers + [Number]
            N = N + 1
        Byte_array_of_numbers = bytearray(str(Array_of_numbers).encode())
        c.send(Byte_array_of_numbers)
        Result = c.recv(4096).decode()
        print(Result)
        c.close()


