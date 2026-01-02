# Remove first n characters from a string

def remove_n(item):
    n = int(input("Enter n value to remove n charcter !"))
    for string in item:
         new_string = string[n:]
         print("Old string",string)
         print("New string",new_string)
    

      
name = ["dhaval","Diamond","Ajju","Gujju","Nothing","12345"]
remove_n(name)
