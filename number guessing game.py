import random
while True:
    def user_guess():
        number=random.randint(1,100)
        guess=0
        while guess != number:
            guess=int(input(f"Pick a number between 1 and {100}: "))
            if guess>number:
                print(guess)
                print("Your guess is too high.")
            elif guess<number:
                print(guess)
                print("Your guess is too low.")
            else:
                print(f"Good job, you guessed {number}")
    def comp_guess():

        low=1
        high=100
        feedback=""
        while True:
            if low!=high:
                guess=random.randint(low,high)
            else:
                guess=low
            response=input(f"Is the number {guess} too high or too low, or correct. Please enter (h),(l) or (c):")
            if response=="h":
                high=guess-1
            elif response=="l":
                low=guess+2
            elif response=="c":
                print(f"Good job, the computer guessed the number {guess}")
                break
    choice=input("Do you want to guess(1), or the computer to guess(2) or quit(Q):")
    if choice=="1":
        user_guess()
    elif choice=="2":
        comp_guess()
    elif choice=="q" or choice=="Q":
        break
    else:
        print("Please enter a valid response.")
