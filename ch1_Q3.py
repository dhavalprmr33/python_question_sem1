#write pythonic code to solve quadatic equation ax**2 + bx + c = 0 by getting input for coefficients from the user

#code start here
import math

a = float(input("enter coefficient a:"))
b = float(input("enter coefficient b:"))
c = float(input("enter coefficient c:"))

if a == 0:
    print("This is not a quadation(a cannot be 0)")
else:
    discriminant = b**2-4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/(2*a)
        root2 = (-b - math.sqrt(discriminant))/(2*a)
        print("two real roots:",root1,"and",root2)

    elif discriminant == 0:
        root = -b/(2*a)
        print("one real root:",root)

    else:
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(-discriminant)/(2*a)
        print("complext root:")
        print(f"{real_part} + {imaginary_part}i")
        print(f"{real_part} - {imaginary_part}i")



