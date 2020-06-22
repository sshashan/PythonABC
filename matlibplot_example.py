print("Matlib plot Example")
import matplotlib.pyplot as pt
x= [1,2,3]
y=[5000,10,50000,]
months=["Jan","Feb","Mar"]
pt.xticks(x,months)
pt.xlabel("Months")
pt.ylabel("Sales")
pt.plot(x,y)
pt.show()

