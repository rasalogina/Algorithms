

employees = ["Kevin", "Linda", "Ian", "Sara", "Jhon"]
print(employees)


x = employees[3]
print(x)

employees[3] = "Rasa"
print(employees)

for employees in sorted(employees[:-1]) + [employees[-1]]:
    print(employees)

age = [26, 30, 34, 24, 20]

for j in range(0, 4):
    for i in range(0, 4):
        if age[i] > age[i+1]:
            swap = age[i]
            age[i] = age[i + 1]
            age[i + 1] = swap
print(age)

from array import *

vals = array('i', [5, 9, -8, 4, 2])
newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)


