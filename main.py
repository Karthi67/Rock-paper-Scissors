rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choose=int(input("enter your chose:"))
import random
random=random.randint(0,2)
if choose==0 and random==1:
  print("Your choose",rock,paper,"loose")
elif choose==0 and random==2:
  print("Your choose",rock,scissors,"loose")
elif choose==1 and random==0:
  print("Your choose",paper,rock,"win")
elif choose==1 and random==2:
  print("Your choose",paper,scissors,"loose")
elif choose==2 and random==0:
  print("Your choose",scissors,rock,"loose")
elif choose==2 and random==1:
  print("Your choose",scissors,paper,"win")
else:
  print(" draw")
