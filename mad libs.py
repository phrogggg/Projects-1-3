while True:
    def madlib_1():
        #creating the variables
        noun=input("Enter a noun: ")
        adjective=input("Enter an adjective: ")
        p_noun=input("Enter a plural noun: ")
        body=input("Enter a body part: ")
        num=input("Enter a number: ")
        place=input("Enter a place: ")
        verb=input("Enter a verb ending in ing: ")
        print(f"I love {verb}. It makes me feel {adjective} and I do it {num} times a day. I especially like to do it in {place} and it makes my {body} feel great. I like {verb} around {p_noun} and with a {noun}")

    def madlib_2():
        #creating the variables
        noun=input("Enter a noun: ")
        adjective=input("Enter an adjective: ")
        p_noun=input("Enter a plural noun: ")
        body=input("Enter a body part: ")
        num=input("Enter a number: ")
        place=input("Enter a place: ")
        verb=input("Enter a verb ending in ing: ")
        print(f"Summer is a {adjective} season! During summer like {verb} and looking at the {noun} and the {p_noun}. I especially like to go to {place} during the summer! I visit {place} {num} times a day, and it makes my {body} feel good.")

    def madlib_3():
        #creating the variables
        noun=input("Enter a noun: ")
        adjective=input("Enter an adjective: ")
        p_noun=input("Enter a plural noun: ")
        body=input("Enter a body part: ")
        num=input("Enter a number: ")
        place=input("Enter a place: ")
        verb=input("Enter a verb ending in ing: ")
        print(f"{verb} is my best sport. I am {adjective} at it. I practice it at {place} {num} times a day. {verb} strengthens my {body}. I especially like {verb} with a {noun} and {p_noun}")
        
    startup=input("Would you like to play story 1,2,3 or press Q to quit: ")

    if startup=="1":
        madlib_1()
    elif startup=="2":
        madlib_2()
    elif startup=="3":
        madlib_3()
    elif startup=="q" or startup=="Q":
        break
    else:
        print("Please select one of the options given")