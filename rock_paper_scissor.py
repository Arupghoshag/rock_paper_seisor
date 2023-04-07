import random

rock = '''
Rock
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
win = '''
Win!
 __      __
( _\    /_ )
 \ _\  /_ / 
  \ _\/_ /_ _
  |_____/_/ /|
  (  (_)__)J-)
  (  /`.,   /
   \/  ;   /
    | ===  |
'''
loose = '''
You lost!

     .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   
 :    .------.    :
  \  '        '  /
   '.          .'
     '-......-'
'''

images = (rock, paper, scissor, win, loose)

your_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
print("My choice:\n")
print(images[your_choice])

computer_choice = random.randint(0, 2)
print("Computer choose:\n")
print(images[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print("You type a invalid number and you lose")
elif your_choice == 0 and computer_choice == 2:
    print(f"You wins!{win}")
elif computer_choice == 0 and your_choice == 2:
    print(f"You lose!{loose}")
elif your_choice > computer_choice:
    print(f"You win!{win}")
elif computer_choice > your_choice:
    print(f"You lose!{loose}")
elif computer_choice == your_choice:
    print(f"It's a draw!")

