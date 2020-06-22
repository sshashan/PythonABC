print("*****BMI calculator*******")
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your height in KG's: "))
bmi=round(weight/(height**2),2)
print("Your BMI is: ",bmi)
if(bmi <= 18.5):
      print("Underweight")
elif(bmi>18.5 and bmi<=24.9):
      print("Normal weight")
elif(bmi > 24.9 and bmi <= 29.9):
      print("Overweight")
else:
      print("Obesity")
