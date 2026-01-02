# # Write a program to check wheather a number is prime or not. Promt the user for input.

# import math

# def is_prime(number):
#     if number <= 1:
#         return print("Error")
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return print(number,"is not prime number.")
    
#     limit = int(math.sqrt(number) + 1)
#     for i in range(3,limit,2) :
#         if number % i == 0:
#             return print(number,"is not prime number.")
#     return print(number,"is prime number")
     
# is_prime(1000)
num = int(input("number : "))
for i in range(2,num):
    if num%i == 0:
        print("not prime ")
        break
else:print("prime ")



  





    



