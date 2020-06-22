print("Factorial program")
num1= int(input("Enter the number for which you want to see the factorial: "))
value=1
num =num1
while(num > 1):
      value=value*num
      num =num - 1

print("Factorial of "+str(num1)+" is: " ,value)



def factorial(n):
      return 1 if(n==1 or n==0) else n * factorial(n-1)
            

print(factorial(num1))


def fact(x):
      if (x == 0):
            return 1
      else:
            return x * fact(x-1)


print(fact(num1))
