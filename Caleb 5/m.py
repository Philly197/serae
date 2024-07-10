def caleb():
    print("A. Drink from your water bottle")
    print("B. Speed up at moderate speed")
    print("C. Speed up at full speed")
    print("D. Rest")
    print("E. Status check")                                                                                                                                                                              
    print("Q. Quit")

import random


print("Welcome to the ALIEN GAME!")
print("You have stolen a UFO to make your way across outer space. The aliens want their UFO back and are chasing you down!")
print("Survive and out run the Aliens!")

done=False
milesTraveled=0
thirst=0
tiredness=0
alienDistance=-100

water_bottle=3

while not done:
    caleb()

    choice=input(' What is your choice?: ').upper()

    if choice == 'Q':
        done=True
       
    
    elif choice == 'A':
        if water_bottle > 0:
            water_bottle -= 1
            thirst = 0 
            print('You drank one of your water bottles.')
        else:
            print('You have no water bottles :(')
    
    elif choice == 'B':
        miles=random.randint(5,12)
        milesTraveled+=miles
        print(f' You sped up at a moderate speed and travled {miles} miles.')
        thirst+=0.5
        tiredness+=1
        alienDistance+=random.randint(4,9)

    elif choice == 'C':
        miles=random.randint(10,20)
        milesTraveled+=miles
        print(f' You sped up at full speed and travled {miles} miles.')
        thirst+=1
        tiredness+=random.randint(1,2)
        alienDistance+=random.randint(6,11)
    
    elif choice == 'D':
        tiredness=0
        print('You are well rested and ready to continue flying.')
        alienDistance+=random.randint(5,10)
    
    elif choice == 'E':
        print(f'Miles travled: {milesTraveled}')
        print(f'Drink in water bottles: {water_bottle}')
        print(f'The aliens are {alienDistance} miles behind you')
    
    else:
        print('Invalid choice please choose again')
    
    if 4 <= thirst <= 6:
        print('You are thirsty.')
    elif thirst >= 6:
        print('You have fainted and the aliens have caught up')

    if 5 <= tiredness < 8:
        print('You are getting tired. ')
    elif tiredness >= 8:
        print('You fell asleep and the aliens caught up!')
        done=True
    if alienDistance >= 0:
        print('The aliens caught up to you game over!' )
        done=True
    elif alienDistance >= -15:
        print('The aliens are getting closer.')
    if milesTraveled >= 100:
        print('You won the game!')
        done=True