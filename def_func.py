print("Defining a function")

def say_hello():
      print("Hello !!!")

def hello_person(person):
      print("Hello",person,"How are you??")
num1=[]
def summ(*arg):
      total=0
      for data in arg:
            total+=data
      return total

print(summ(10,2,7,8))

def mul(num1,num2):
      total= num1*num2
      return total

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number"))
output=mul(num1,num2)
print("The product of ",num1,"and",num2,"is :",output)

