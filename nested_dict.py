print("Nested dictionary Example")

persons={1:{"fname":"sujay","lname":"shashank","mobno":{1:7744,2:9632}}
         ,2:{"fname":"sujay2","lname":"shashank2","mobno":{1:77442,2:96322}}
         ,3:{"fname":"sujay3","lname":"shashank3","mobno":{1:77443,2:96323}}
             ,4:{"fname":"sujay4","lname":"shashank4","mobno":{1:77444,2:96324}}}

for empid in persons:
      print(persons[empid])
      for data in  persons[empid]:
            print(data)
