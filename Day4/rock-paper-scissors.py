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
import random 

choses = [rock, paper, scissors]
user_chose = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. \n"))
computer_chose = random.randint(0,2)

if user_chose >= 3 or user_chose < 0:
    print("You typed a invalid number. You lose.")
else:
    print(choses[user_chose])
    print("Computer chose:")
    print(choses[computer_chose])

    if user_chose == computer_chose:
        print("Tied")
    elif user_chose == 0:
        if computer_chose == 1:
            print ("You lose")
        else:
            print("You win!")
    elif user_chose == 1:
        if computer_chose == 2:
            print ("You lose")
        else:
            print("You win!")
    elif user_chose == 2:
        if computer_chose == 0:
            print ("You lose")
        else:
            print("You win!")
