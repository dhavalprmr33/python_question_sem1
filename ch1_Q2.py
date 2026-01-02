#Implement the python program to claculate total and average marks bassed on input.

#code start here
def subject():
    math = int(input("enter math marks:"))
    science = int(input("enter science marks:"))
    english = int(input("enter english marks:"))

    total = math + science + english

    average = total/3

    print("Your total is", total,"and average is", average) 

s1 = subject()
