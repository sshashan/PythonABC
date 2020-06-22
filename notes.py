print("Program to get the minimum number of notes")

t=int(input("Enter the money count"))
print("Enter the amount")
amounts=[]
while( len(amounts) < t):
      amounts.append(int(input()))


notes=[50,10,5,2,1]
no_of_notes=[]
for i in amounts:
      num_of_100=int(i/100)
      no_of_notes.append(num_of_100)
      remaining= i%100
      num_of_50=int(remaining/50)
      remaining_1=remaining%50
      number_of_10=int(remaining_1/10)
      reamining_2=remaining_1%10
      number_of_5=int(reamining_2/5)
      remaining_3=reamining_2%5
      number_of_2=int(remaining_3/2)
      remaining_4=remaining_3%2
      number_of_1=remaining_4
      print(num_of_100+num_of_50+number_of_10+number_of_5+number_of_2+number_of_1)

      
            
            
            
            
