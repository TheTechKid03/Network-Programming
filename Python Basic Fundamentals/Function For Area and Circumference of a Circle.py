def Area_and_Circumference_of_a_Circle():
    Pie = 3.14
    Radius = input("What is the radius of the circle?: \n")
    Radius2 = int(Radius) * int(Radius)
    Area = Pie * Radius2
    Circumference = (2 * Pie) * int(Radius)
    print("The area of the circle is: ", Area)
    print("The circumference of the circle is: ", Circumference)


Area_and_Circumference_of_a_Circle()
