#If the ram, sam, and khan are input through keyboard. write a python program to determine the eldest and youngest of the three.

def determine():

    first_name, first_age = input("enter first person name:"),int(input("enter first person age:"))

    second_name, second_age = input("enter second person name:"),int(input("enter second person age:"))
    
    third_name, third_age = input("enter third person name:"),int(input("enter third person age:"))
    
    if first_age >= second_age and third_age:
        print(first_name,"is eldest.")
    elif second_age >= first_age and third_age:
        print(second_name, "is eldest.")
    else:print(third_name, "is eldest.")

    if first_age <= second_age and third_age:
        print(first_name,"is youngest.")
    elif second_age <= first_age and third_age:
        print(second_name, "is youngest.")
    else:print(third_name, "is youngest.")

determine()