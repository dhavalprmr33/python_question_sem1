# write a python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter n value --> "))
nlist = []
while True:
    for i in range(1,n+1):
        nlist.append(n*i)
    break
print(sum(nlist))
