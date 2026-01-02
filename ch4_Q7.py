# Given a two list of number, write a program to create a new list such that the new list such that the new list should contain odd numbers from the first list and even number from the second list.
# given:
# list1 = [10,20,25,30,35]
# list2 = [40,45,60,75,90]

def first_list_even_second_list_odd(list1,list2):
    new_list = []
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)

    for i in list2:
        if i % 2 == 0:
            new_list.append(i)
    
    print(new_list)

list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]
first_list_even_second_list_odd(list1,list2)