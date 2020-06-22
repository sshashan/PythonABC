print("This program will show you the result based on your grade and attendance")
data_valid = False

while data_valid == False:
      grade1=input("Enter your grade1 marks:")
      try:
            grade1=float(grade1)
            if(grade1 > 0 and grade1 < 10):
                  data_valid= True
            else:
                  print("Grade should be in between 1 to 10")
      except:
            print("Invalid data format")

data_valid = False

while data_valid == False:
      grade2=input("Enter your grade2 marks:")
      try:
            grade2=float(grade2)
            if(grade1 > 0 and grade1 <= 10):
                  data_valid= True
            else:
                  print("Grade should be in between 1 to 10")
      except:
            print("Invalid data")

total_classes = 100
absence = int(input("Enter the number of classes you missed: "))
print(grade1)
print(grade2)
print("attendance",str(total_classes-absence)+'%')

            
