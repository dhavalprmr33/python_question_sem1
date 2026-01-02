# Check if the first and last number of list is the same

def check_first_last(**list_of_number):
    if list_of_number[0] == list_of_number[-1]:
        print("The first and last number of list is the same.")
    else:
        print("The first and ast number of list is not same.")

# Exemple
list1 = [1,2,3,4,5,6]
list2 = [2,3,4,2]

check_first_last(list1,list2)
