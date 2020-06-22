print("Quiz Game")
import requests
import json
import random
while(True):
      r=requests.get("https://opentdb.com/api.php?amount=1&category=24")
      rtext=r.text
      rtext_dict=json.loads(rtext)
      input("To start the game press Enter")
      print("Q:",rtext_dict['results'][0]['question'])
      print("Your options are:")
      option=rtext_dict['results'][0]['incorrect_answers']
      c_ans=rtext_dict['results'][0]['correct_answer']
      option.insert(random.randint(0,3),c_ans)
      j=1
      for i in option:
            print(str(j)+":"+i)
            j +=1

      answer=input("Enter your answer:")
      if(answer.lower()==c_ans.lower()):
            print("You are correct!!!!")
            q=input("Do you want to play again,enter quit to quit the game....")
            if(q.lower()=="quit"):
                  break

      else:
            print("Correct answer is :",c_ans)
            q=input("Do you want to play again,enter quit to quit the game....")
            if(q.lower()=="quit"):
                  break
      

print("Game over")
      
