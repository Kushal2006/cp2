print("Name: Kushal Dubey")
print("Roll No: 24BEE110")
import random
list =[random.randrange(-15,15) for _ in range (10)]
squared =[]
for i in list:
    f =i**2
    squared.append(f)
print(squared)