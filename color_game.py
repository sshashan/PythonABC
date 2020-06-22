print("**** Welcome to the color guessing game*******")

colors=["red","blue","green","orange","white","yellow","black"]
import random
while True:
      index= random.randint(0,len(colors)-1)
      correct_color=colors[index]
      user_color=input("Enter the colour you are guessing:").lower()
      while True:
            if(user_color == correct_color):
                             break
            else:
                  user_color=input("Nope, try again:")
                  
      print("You guessed it correctly!!")
      play_again=input("Do you want to play more?? Type 'no' to quit:")
      if(play_again.lower()=='no'):
                                   break
                                   
                             
