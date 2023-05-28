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
import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

if player == 0:
  print("You chose: \n" + rock)
  if computer == 0:
    print("The computer chose: \n" + rock)
    print("\nIt's a draw!")
  elif computer == 1:
    print("The computer chose: \n" + paper)
    print("\nThe computer wins!")
  else:
    print("The computer chose: \n" + scissors)
    print("\nYou win!")
elif player == 1:
  
  print("You chose: \n" + paper)
  
  if computer == 0:
    print("The computer chose: \n" + rock)
    print("\nYou win!")
    
  elif computer == 1:
    print("The computer chose: \n" + paper)
    print("\nIt's a draw!")
    
  else:
    print("The computer chose: \n" + scissors)
    print("\nThe computer wins!")
else:
  print("You chose: \n" + scissors)
  
  if computer == 0:
    print("The computer chose: \n" + rock)
    print("\nThe computer wins!")
    
    
  elif computer == 1:
    print("The computer chose: \n" + paper)
    print("\nYou win!")
    
  else:
    print("The computer chose: \n" + scissors)
    print("\nIt's a draw!")