import random
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
game_images=[rock,paper,scissors]
#Write your code below this line 👇
your_choice=int(input("what do you want to choose: type 0 for rock,type 1 for paper type 2 for scissors \n"))
if your_choice>=3 or your_choice<0:
    print("you entered a wrong choice")
else:
    print(game_images[your_choice])
    computer_choice=random.randint(0,2)
    print(f"computer choice is: \n"
          f"{game_images[computer_choice]}")

    if computer_choice==your_choice:
        print("it's a draw")
    elif computer_choice==2 and your_choice==0:
        print("you  win the game")
    elif computer_choice>your_choice:
        print("computer won the game")
    elif computer_choice==0 and your_choice==2:
        print("computer won the game")
    elif your_choice>computer_choice:
        print("you  win the game")
