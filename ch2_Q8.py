# Write a programm to print sum of the following series 1 + 1/2 + 1/3 + . ..... 1/n 

while True:
    number = int(input("Enter n number --> "))
    n_list = []
    for i in range(number+1):
        if i >= 1:
         n_list.append(1/i)
    break    
print("That is list of following series :",n_list)
print("That is sum of all following series :",sum(n_list))



