print("Name: Kushal Dubey")
print("Roll No: 24BEE110")
import random 
list =[]
def remove (l):
    l =  [random.randrange(1,30) for _ in range (50) ]
    f=[]
    for i in l:
        if i not in f:
            f.append(i)
    f.sort()

    print(f"The list after removing all the reccuring elements is {f}")
remove(list)
    
