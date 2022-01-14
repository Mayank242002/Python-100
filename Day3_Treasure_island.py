print('''
    
     |                       
  ___| |__   ___  ___ _ __ ___ 
 / __| '_ \ / _ \/ _ \ '__/ __|
| (__| | | |  __/  __/ |  \__ \
 \___|_| |_|\___|\___|_|  |___/

''')

print("Welcome To Treasure Island.Your Misson is to find the Treasure")
choice=input('You\'re at a cross road.Where do you want to go Type "left" or "right" ')
if (choice=="left"):
    choice=input('Yoo came to lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.TYpe "swim" to swim')
    if (choice=="wait"):
        choice=input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. which colour do you choose?')
        if (choice=="blue"):
            print("You came to the house of beasts.Game over")
        elif (choice=="red"):
            print("Your reached to the monsters.Game over")
        else:
            print("You win")
    else:
        print("Shark!!! You got eaten. Game over")
else:
    print("You idiot!! Game over")
