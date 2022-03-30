import random
import time


def game():   
    user_counter = 0
    comp_counter = 0   
    while True:       
        user=input("Please select Rock (R), Paper (P), Scissors (S), Lizard (L) or Spock (O): ")
        comp=random.choice(["R","P","S","L","O"])
        if user == "Q" or user == "q":
            if user_counter>comp_counter:
                print(f"The final score is {user_counter} to {comp_counter}. Good job, you won")
            elif user_counter<comp_counter:
                print(f"The final score is {user_counter} to {comp_counter}. Too bad, you lost")
            elif user_counter==comp_counter:
                print(f"The final score is {user_counter} to {comp_counter}. You and the computer tied")
            print("Exiting in 5 seconds")
            time.sleep(5)
            exit()
        if user==comp:
            print("You have tied.")
        elif (user == "R" and comp=="S") or (user == "r" and comp=="S") or (user == "R" and comp=="L")\
        or (user == "r" and comp=="L") or (user == "S" and comp == "P") or (user =="s" and comp == "P")\
        or (user == "S" and comp == "L") or (user == "s" and comp == "L") or (user == "P" and comp == "R")\
        or (user == "p" and comp == "R") or (user == "P" and comp =="O") or (user == "p" and comp =="O")\
        or (user == "L" and comp == "P") or (user =="l" and comp =="P") or (user == "L" and comp == "O")\
        or (user == "l" and comp =="O") or (user == "O" and comp == "R") or (user == "o" and comp == "R")\
        or (user == "O" and comp =="S") or (user == "o" and comp =="S"):
            user_counter = user_counter + 1
            print(f"Good Job, You Won. The score is now: {user_counter} to {comp_counter}")
        else: 
            comp_counter = comp_counter + 1
            print(f"Too Bad, You Lost. The score is now: {user_counter} to {comp_counter}")
        
while True:
    user_startup=input("Do you want to play Rock Paper Scissors Lizard Spock (Y) or quit at anytime by pressing (Q): ")
    if user_startup == "Y" or user_startup == "y":
        game()
    elif user_startup == "Q" or user_startup == "q":
        break
    else:
        print("Please enter a valid command.")
