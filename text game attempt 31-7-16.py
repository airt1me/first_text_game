import random
import time

def start_intro():
    print('You have just woken up and are not sure where you are. \n' 
          'You look around the room you are in, it is wooden, unremarkable, \n'
          'and dirty, there is a door leading out of the room to your left \n'
          'and a window to your right \n'
          ' ')

    time.sleep(5)

def first_decision():
    print('You stand up, what do you want to 1) open the door 2) go look out \n' 
          'the window or 3) search the room? Please choose 1, 2 or 3.')
    action = ''
    while action != '1' and action != '2' and action != '3':
        print('Please choose 1, 2 or 3')
        action = input()
        if action == '1': # need to add whatever item is collected to a data structure
            print('You open the door, you see that you are in a forest and you \n'
                  'step outside for a better look and realise you were in a wooden \n'
                  'cabin, there is an axe leaning against the cabin, you pick \n'
                  'it up as it may be useful')
        elif action == '2':
            print('You go to the window, you see you are in a forest, you notice \n' 
                  'a knife by the window, it might prove useful so you take it and \n'
                  'then head out the door')
        elif action == '3':
            print('You search the room, in a drawer you find some money, 10 gold \n' 
                  'pieces, most like currency, you put them in your pocket then head \n'
                  'out the door')

def storyline_one():
    time.sleep(5)
    print('\n'
          'As you take a step away from the cabin you hear a shout, to your right \n'
          'there are four men running towards you looking angry, you start running \n'
          'in the opposite direction. You run as fast as you can for some time, then \n'
          'slow down, you can\'t hear them behind you anymore and you notice there are \n'
          'buildings up ahead, it looks like a small village or a town, you approach \n'
          'it cautiously...')
    time.sleep(8)
    print('A voice calls out, the men pursuing you have caught up and they don\'t sound \n'
          'far behind you, you move up to the nearest house...')
    time.sleep(3)

def second_decision():
    print('\n'
          'What do you want to do next either 1) knock on the door to try and talk the \n'
          'person inside into letting you in and hiding you or 2) if you have a knife \n'
          'use it to jimmy open the lock and let yourself in')
    action = ''
    while action != '1' and action != '2':
        print('Please choose 1 or 2')
        action = input()
        if action == '1':
            print('You knock on the door after a minute a man answers, he is unwilling \n'
                  'to let you in')
        elif action == '2': # add if statement to check if you have a knife
            print('You quietly move to the door and manage to open it, there is a man \n'
                  'sleeping in a chair in front of you, you close the door and sneak \n'
                  'into the bedroom and slide under the bed')


start_intro()

first_decision()

storyline_one()

second_decision()
