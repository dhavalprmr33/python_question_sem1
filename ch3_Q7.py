# write a program to create a function show_employee() using te following conditions.
# It should accespt the employee's name and salary and display both
# it the salary is missing in the function call then assing default value 9000 to salary

class show_employee():
   def __init__(self,name,salary = 9000):
      self.name = name
      self.salary = salary

employee1 = show_employee("Chaman")
print(employee1.name,employee1.salary)
employee2 = show_employee("naman",100000)
print("name:",employee2.name,"salary:",employee2.salary)