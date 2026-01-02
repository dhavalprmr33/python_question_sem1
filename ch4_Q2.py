# print character from a string that are present at an even index

def show_even_index(items):
    for string in items:
        if items.index(string) % 2  == 0:
            print(string)



list1 = ["Gujju","Ajju","Munnu"]
list2 = [0,1,2,3,4,5,6,7,8,9]
show_even_index(list1)
show_even_index(list2)