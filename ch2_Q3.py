#Write a program to promt for a score betweenw 0.0 and 1.0 if the score is out of range. print an error.if the score is between 0.0 and 1.0, print a grade using the following table

def score():
    score = float(input("enter a score:"))
    if score <= 0.0 or score >= 1.0:
        print("ERROR!")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else: print("F")

score()