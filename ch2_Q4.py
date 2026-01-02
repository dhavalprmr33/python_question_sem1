#Write a program to display the fibonacci seqquence up to nth tearm where n is provided by the user.

def fibonacci(n):
    a,b = 0,1
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(a)
    else:
        print("Fibonacci sequence up to", n, ":")
        count = 0
        while count < n:
            print(a, end="")
            nth = a + b
            a = b
            b = nth
            count += 1

num = 10
fibonacci(num)


