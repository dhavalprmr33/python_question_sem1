# Display three string "Name","Is","James" as "Name**Is**James"

def string(*strings):
    print("**".join(strings))

string("Name","Is","James")


