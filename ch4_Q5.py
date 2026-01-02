# Write Python program to sort words in a sentence in decreasing oredr of their length. Display the sorted words along with thier lenngth.

def sort_decreasing(sentence):
    words = []
    word = ""
    for ch in sentence:
        if ch != " ":
            word += ch
        else:
            words.append(word)
            word = ""
    words.append(word)
    
    words = sorted(words,reverse=True)
    for i in words:
        print(i,len(i))

sentence = "i am dhaval"
sort_decreasing(sentence)





 



    
    
  
    
















        
        

        
        
