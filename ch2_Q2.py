#write a python program to find the given number is odd or even.

def find_num_odd_even():
    number = int(input("Enter a number:"))
    if number / 2 == 0:
        print(number, "is even.")
    else:print(number, "is odd.")

find_num_odd_even()