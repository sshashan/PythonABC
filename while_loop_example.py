print("Guess Program using while loop")

import random
number = random.randint(0,10)
guess = int(input("Enter a number :"))

while (True):
      if(number == guess):
            break
      else:
            guess = int(input("Nope, try again :"))
print("You guessed it correctly, the number is ", number)
