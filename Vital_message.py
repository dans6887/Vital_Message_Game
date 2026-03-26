import os
import random
import string

import time



def vital_message_game():
    os.system('cls||clear') #clears the screen before the game starts

    print("VITAL MESSAGE")
    print()

    while True:
        #asks use how difficult they want the game and assigns the number to the difficulty variable
        difficulty = int(input("How Difficult? (4-10)"))
        if difficulty>=4 or difficulty<=10:
            break

   

    m = ""

    for i in range(difficulty):
        m += random.choice(string.ascii_uppercase)

    os.system('cls||clear') #clears the screen

    print("SEND THIS MESSAGE: ")
    print()
    print(m)

    time.sleep(5) #wait five seconds
    os.system('cls||clear') #clears the screen

    answer = input("Enter your answer then press [ENTER]: ").upper()

    if answer == m:
        print("Message Correct...")
        time.sleep(2)
        print("The robot war is over.")
        exit
    elif answer != m:
        print("Message incorrect...")
        time.sleep(2)
        print("The robot invasion has started")
        vital_message_game()

if __name__ == "__main__":
    vital_message_game()

