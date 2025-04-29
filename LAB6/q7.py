print("Name: Kushal Dubey")
print("Roll No: 24BEE110")

tuple = (1, 2, 3, 4)
newtuple = ()


for i in range(len(tuple)):
    if i == 2:  
        continue
    newtuple += (tuple[i],)

print("Tuple after deletion:", newtuple)
