
import os

import functions

filehandle = open("./input.txt",'r')

lines = filehandle.readlines()

# print(lines)

listOfInts = []

for s in lines:
    i = int(s)
    listOfInts.append(i)

output=map(functions.calcTotalFuel,listOfInts)
total = sum(output)
print(type(total))
