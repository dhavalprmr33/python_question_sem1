# Check if the items in list are sorted in asceding or descending oreder and print suitable messages accordingly.otherwise, print"Items in list are not sorted"

def check_order(items):
    if items == sorted(items):
        print("Items in list are sorted in asceding order.")
    elif items == sorted(items,reverse=True):
        print("Items in list are sorted in desceding order.")
    else:print("Items in list are not sorted")

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]
list3 = [1,5,2,3,4]
list4 = []

check_order(list1)
check_order(list2)
check_order(list3)
check_order(list4)



   
