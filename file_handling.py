print("File handling program")
#f=open("file_handling.txt","w")
#f.write("This is an write example")
#f.close()
#f=open("file_handling.txt","a")
#f.write("\n This line is added in append mode")
#f.close()


f=open("file_handling.txt","r")

for i in f:
      print(i)

