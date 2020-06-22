print("Program to print the result")

grade1=float(input("Enter your first grade:"))
grade2=float(input("Enter your second grade:"))
absence = int(input("Enter the number of classes you were absent:"))

total_class=100

avg_grade=round((grade1+grade2)/2,2)
attendance = (total_class - absence)/total_class

print("Your grade is ",avg_grade)
print("Your attendance % is :",str(round(attendance,2)*100)+'%')

if(avg_grade > 6):
      if(attendance > .8):
            print("You are passed")
      else:
            print("Your attendance is low")
elif(attendance > .8):
      print("Your attendace is good but your grade is lower than 6")
else:
      print("You are good at nothing")
