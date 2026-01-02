# Write a function which receives a variable number of strings as arguments. find unique characters in each strings.

def unique_characters(*strings):
    result = {}

    for s in strings:
        result[s] = set(s)
    return result

output = unique_characters("dhaval","deepak","diamond")
for string,chars in output.items():
    print(f"{string} -> {chars}")

