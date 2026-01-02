# Write a python program using functions too find the value of nPr and nCr without using inbuilt factorial() function

def nPr():
    n = int(input("Enter n value : "))
    r = int(input("Enter r value : "))
    count=1
    while True:
        for i in range(1,n+1):
            count = count * i
        break
    n_factorial = count
   
    count=1
    while True:
        for i in range(1,n-r+1):
            count2 = count * i
        break
    r_factorial = count2

    nPr = n_factorial / r_factorial
    print(nPr)
print("---> nPr() <---")
nPr()

def nCr():
    n = int(input("Enter a n value : "))
    r = int(input("Enter a r value :  "))
    count=1
    while True:
        for i in range(1,n+1):
             count = count * i
        break
    n_fact = count

    count2=1
    while True:
        for i in range(1,r+1):
            count2 = count2 * i
        break
    r_fact = count2

    count3=1
    while True:
        for i in range(1,n-r+1):
            count3 = count3 * i
        break
    n_r_fact = count3
    second_step = r_fact * n_r_fact
    nCr_ = n_fact / second_step

    print(nCr_)

print("---> nCr() <---")
nCr()
