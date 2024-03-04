# Importing crucial libraries
import socket

# Variables for Later Use
Server_Ip = input("Enter The Socket IP Address you want to assign: ")
Port_number = input("Enter The Socket Port you want to assign: ")
Addition_of_Numbers = 0
N = 0

# Socket Important Information
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((str(Server_Ip), int(Port_number)))
s.listen()

Menu = ("|--------------------------------------------------------|\n"
        "|            Simple Mathematical Calculator V11          |\n"
        "|--------------------------------------------------------|\n"
        "|                                                        |\n"
        "|    1. Addition Between x amount of Numbers  ( < 5 )    |\n"
        "|                                                        |\n"
        "|    2. Multiplication Between two Numbers               |\n"
        "|                                                        |\n"
        "|    3. Division between two Numbers                     |\n"
        "|                                                        |\n"
        "|    4. Subtraction Between x amount of Numbers ( < 5 )  |\n"
        "|                                                        |\n"
        "|    5. The Square of Number x                           |\n"
        "|                                                        |\n"
        "|--------------------------------------------------------|\n").encode()

# While loop to keep server running indefinitely
while True:
    c, Client_address = s.accept()
    c.send(Menu)
    Option = c.recv(256).decode()

    if int(Option) == 1:
        Size_of_loop = c.recv(256).decode()
        Array_of_numbers = eval(c.recv(4096).decode())
        while N < int(Size_of_loop):
            Addition_of_Numbers = Addition_of_Numbers + int(Array_of_numbers[N])
            N = N + 1
        Computation = ("The Addition of all the number is: " + str(Addition_of_Numbers)).encode()
        c.send(Computation)
    c.close()

