def Average_of_6_numbers():
    N = 0
    Average = 0
    while N < 6:
        Num = input("Enter a number: \n")
        Average = Average + int(Num)
        N = N + 1
    print("The Average of those 6 number are: ", Average)


Average_of_6_numbers()
