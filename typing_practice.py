import time as t
import matplotlib.pyplot as plt

times=[]
mistakes=0
while(len(times) < 5):
      input("Press enter to start")
      start_time= t.time()
      word = input("Enter the word five times:")
      end_time=t.time()
      time_elapsed=end_time-start_time
      times.append(time_elapsed)
      if((word).lower() !="programming"):
            mistakes += 1

print("You made",mistakes,"mistakes")

x=[1,2,3,4,5]
y=times
xplot=["1","2","3","4","5"]
plt.xticks(x,xplot)
plt.xlabel("No of attempts")
plt.ylabel("Time taken")
plt.plot(x,y)
plt.show()
