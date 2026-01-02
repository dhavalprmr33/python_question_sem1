# Write a program to repeatedly check for the largesst number until the user enters "done" 

def number():
    num1 = int(input("Enter First number:"))
    num2 = int(input("Enter Second number:"))
    if num1 >= num2:
        print(num1,"is largest")
    else: print(num2,"is largest")


    while True:
        user = str(input("enter Done/Reuse(Done for exit!):"))
        if user == "Done":
            print("Program Close!")
            break
        else:
            print("User reuse the programm")
            number()

number()





           
        

    