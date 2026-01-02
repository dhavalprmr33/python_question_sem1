# Write a programm to check palindrome Number

while True:
    number = (input("Enter number value to check number is palindrome or not : "))
    num_list = []
    for char in number:
        num_list.append(char)  
    break
new = list(reversed(num_list))
if num_list == new:
    print(number,"is palindrome number. ")
else:print("Value error or negitive values input given !")
number = int()
print(type(number))