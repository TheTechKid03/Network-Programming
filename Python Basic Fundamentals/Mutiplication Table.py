Num = input("Enter the number that you want to see the multiplication table of: ")
N = 0

while N < 13:
    Answer = int(Num) * int(N)
    print(Num, " ", "x", " ", int(N), " ", "=", Answer)
    N = int(N) + 1
