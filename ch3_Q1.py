# Describe the syntax for the following functions and explain with an example.
# abs() max() divmod() pow() len() 
print("---> abs() <---")
x = abs(19.17j)
print(x)
y= abs(19+23j)
print(y)

print("\n---> max() <---")
x = [1,2,3,4,5,6,7,8,9,10]
print("Minimum value : ",min(x))
print("Maximum value : ",max(x))

print("\n---> divmod() <--- ")
x = 10
y = 5
print(divmod(x,y))
x = 13.5
y = 7.8
print(divmod(x,y))

print("\n---> pow() <---")
a = pow(5,2)
b = 5
c = 2
print(a,pow(b,c))

print("\n---> len() <---")
name = "DhavalParmar"
print(name,len(name))