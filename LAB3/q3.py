print("Name: Kushal Dubey")
print("Roll No: 24BEE110")
a = input("Enter the first string")
b= input("Enter the second string")
isthere=    False
for i in a:
   
    if i in b :
     isthere=True
   
if isthere:
   print("The string is present in other")
else:
   print("The string is not present in another")