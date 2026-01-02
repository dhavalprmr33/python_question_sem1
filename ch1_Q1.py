#Create a program that asks the user to enter their name aand thier age.Print out a message addressed to to them that tells that they will turn 100 years old.

#Code start here

def messager():
    name = str(input("enter your name:"))
    age = int(input("enter your aga:"))
    turnyear =2025 - age + 100
    print(name, "you will turn 100 years old in", turnyear)
 
#I/O
s1 = messager()
    
