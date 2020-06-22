print("This Program returns the birth month")
birthdate = input("Enter the Date of birth in format DD-MM-YYYY:")
months=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

month = int(birthdate[3:5]) -1
print("Your month of birth is:",months[month])
