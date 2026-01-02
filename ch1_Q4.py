#find the area and perimeter of a circle using function. prompt the user fior input

#code start here
import math
def circle(r):
    area = math.pi * r * r
    print("circle area is",area)
    perimeter = 2 * math.pi * r
    print("circle perimeter is",perimeter)

s1 = circle(4)
s2 = circle(5)

    