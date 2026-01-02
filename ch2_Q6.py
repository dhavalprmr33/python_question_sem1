#Write a program to find the sum of all odd and even numbers up to a number specified by the user.

def number():
    number = input("enter a number (n):")
    n = int(number)
    my_list = list(range(n + 1))
    even_num_list = []
    odd_num_list = []

    for i in my_list:
        if i % 2 == 0:
           even_num_list.append(i)
        else: odd_num_list.append(i)
    
    print("Even number list",even_num_list,"Sum of even number:",sum(even_num_list))
    print("Odd number list",odd_num_list,"sum of odd number", sum(odd_num_list))



number()

  







    
        
 