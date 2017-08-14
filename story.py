user_response = 0 

def begin_story(): 
    user_name = input("Please enter your name")
    print(user_name, 'you wake up at mid-night and you hear growling outside, turns out its time for the zombie apocalypse.What is the first thing you do?')
    print('Enter the number to your decision.')
    user_response = input('1. You scream of terror. \n2. You climb the roof and put and place a help sign. \n3. You grab a knife and start killing them. \n4. You grab your phone and see whos alive. \n5. Kill Yourself. \n6. Try making a cure. \n7. Make sure your family is safe. \n8. Meet up with your friends. \n9. Do absolutely nothing. \n10. Continue your normal day.')
    house()

def house():
    #1. You press the door open button to exit as soon as possible. 
    if (user_response == 1):
        print("zombies start bombarding your place. What do you do?")
        user_response = input("1. You decide to commit suicide")

    #2. You punch the man. 
    elif (user_response == 2):
        print('your sign is finished and 1 month later nobody came and you starved.')
        user_response = input("R.I.P")

    #3. You say hi to him'
    elif (user_response == 3):
        print('Your turn out to be the best zombie killer passing on your legacy to your zombies kids.')

    #3. You say hi to him'
    elif (user_response == 4):
        print('once you power your phone it sent a powerful electric wave attracting hordes of zombies.')
        
            #3. You say hi to him'
    elif (user_response == 5):
        print('Nope you cant take the easy way out.')

    #3. You say hi to him'
    elif (user_response == 6):
        print('You attempt making a cure but instead the cure made you into one of them.')

    #3. You say hi to him'
    elif (user_response == 7):
        print('Your family is ok but your mom is sick possible infected What do you do.')
        user_response = input("1. You decide do give her your last goodbye")
        user_response = input("2. You keep her in this world later get your entire family infected")

    #3. You say hi to him'
    elif (user_response == 8):
        print('You planned to meet your friends in school but none of them made it. What do you do')
        user_response = input("1.You leave before you get spotted ")
        user_response = input("2.You find their bodys to honer them, and you commit suicide")

    #3. You say hi to him'
    elif (user_response == 9):
        print('Stay in your room staring at blank space thinking about what to do.')
        user_response = input("1.You die from deep thought")
        user_response = input("1.You decide to play xbox")

    #3. You say hi to him'
    elif (user_response == 10):
        print('You go on with your day which doesnt end well for you.')

user_response = 0
begin_story()
