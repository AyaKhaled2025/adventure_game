# You can use this workspace to write and submit your adventure game project.
# Run the game by entering python3 adventure_game.py in the terminal
import time  # import time to sleep some times
import random  # import random to select random objects
# Configure List Of Objects
Places = ['Forest','Desert','House' ]
Weapons = ['Glaive','Javelin','Guisarme','Halberd','Cleaver','Cutlass','Falchion','Lance','Crossbows','Longbows','Dagger','Switchblade']
Forest_Monsters = ['Panda','Lemur','Tiger','Cat','Dinosaurs','Dragons','Chicken','Chimpanze','Gorilla']
Desert_Monsters = ['Fox','Scorpion','Kangaroo','Camel','Jerboa','Armadillo','Ostrich','Hamster','Flamingo','Tortoise','Bat','Caracal','Eagle','Lizard','Gecko']
House = ['Eat','Drink','Sleep','Watch Movie']
Game_Result = ['Win','Lose']
# End Configuration
# Define Function To Print Messages

def PrintSleep(msg,seconds):
    print(msg +'\n')
    time.sleep(seconds)
PrintSleep("Try to place this advanced game because it is too fun " ,2)
PrintSleep("Adventure game is a collection of exciting experiences" ,2)
print()
time.sleep(2)
print()
time.sleep(2)
print('Adventure game can be provided by some unusual activities ')
time.sleep(2)
name = input ('Please Enter Your Name To Start Game \n')
print('Please Choose Which Place you want to play \n')
for place in Places:
     print(place)
     time.sleep(1)
Choice = ''
while Choice not in Places:
   msg ='Give me your choice for forest write f or forest or 1\n for desert write d or desert or 2\n for house write h or house or 3\n'
   Choice=input('\n')
   if Choice.lower() == 'Forest'.lower() or Choice.lower()  == 'F'.lower() or Choice == '1':
       Choice ='Forest'
   elif Choice.lower() == 'Desert'.lower() or Choice.lower()  == 'D'.lower() or Choice == '2':
       Choice ='Desert'
   elif Choice.lower()  == 'House'.lower()  or Choice.lower() == 'H'.lower() or Choice == '3':
       Choice  ='House'
   else:
       Choice = ''
time.sleep(2)
print('you have a weapon ')
weaponchoosed = random.choice(Weapons)
print(weaponchoosed)
changerequest = input('would you like to change weapon\n')
if changerequest == 'yes':
    weaponchoosed = random.choice(Weapons)
print(weaponchoosed)
print('\nyou now in '+ Choice + 'and you have a Weapon ' + weaponchoosed)
time.sleep(1)
print('now you see front of you ')
if Choice == 'Forest':
    print(random.choice(Forest_Monsters))
if Choice == 'Desert':
    print(random.choice(Desert_Monsters))
if Choice == 'House':
    print(random.choice(House_Monsters))
time.sleep(2)    
print('Use weapon to kill monster' , 2)

print('you' + random.choice(Game_Result))
time.sleep(2)
print ('Game Over')
