"Program to print names"

names=[]
while (len(names) < 8):
      name=input("Enter the name:")
      names.append(name)
import random
index=random.randint(0,8)
print(names[index])
