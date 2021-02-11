from array import *
from ndarray import *

employees = ["Kevin", "Linda", "Ian", "Sara", "Jhon"]
print(employees)

employees[3] = "Rasa"
print(employees)

for employees in sorted(employees[:-1]) + [employees[-1]]:
    print(employees)


age = array('i', [5, 9, -8, 4, 2])

for i in range(4):
    if age[i] > age[i+1:]:
        swap =age[i]
        age[i] = age[i+1]
        age[i+1] = swap
print(age)





