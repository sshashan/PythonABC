print("Calculator for Addition/Deletion/Multiplication/Subtraction")

print("Select the operation type")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

user_opt=int(input("Enter your operation number: "))
num1= int(input("Enter the first number :"))
num2= int(input("Enter your second number:"))
if (user_opt==1):
             print("Sum of two numbers are: ",num1+num2)
elif (user_opt==2):
      print("Subtraction of two numbers are:", num1-num2)
elif (user_opt==3):
      print("Multiplication of two numbers are :",num1*num2)
elif (user_opt==4):
      print("Division of two numbers are: ",num1/num2)

else:
      print("Enter a valid option")
