import random


computer_choice = random.choice(('rock', 'paper', 'scissors'))


print("Enter selection (rock, paper, or scissors):")
user_choice = input().lower()

if user_choice in ('rock', 'paper', 'scissors'):
 
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie.")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose.")
else:
    print("This is not a valid object selection.")
        
       