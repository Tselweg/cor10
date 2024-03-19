#random numbers!
import random
number = random.randint(1, 20)
print(number)
import numpy as np

listOfRandomnumbers = []
for i in range(100):
    n = random.randint(1, 20)
    listOfRandomnumbers.append(n)

print(listOfRandomnumbers)


list2 = [random.randint(1,20) for i in range (100)]
print(list2)
print("lenght of list2 is", len(list2))


total=0 

for number in listOfRandomnumbers:
    total= total + number 

print("total: ", total)
#

totalsum = sum(listOfRandomnumbers)
print("total: ", total, totalsum)
