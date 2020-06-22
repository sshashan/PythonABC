print("This program gets the property of a person")

person={"name":"Sujay Shashank","age":30,"phone":7744812925,"gender":"Male","address":"Mana tropicale"}
print("What information you want??")
key= input("Enter the property (name,age,phone,gender,address):").lower()

result=person.get(key,"Info what you are looking for is not present")
print(result)
