import random
import time

def start_intro():
    print('You have just woken up and are not sure where you are. \n' 
          'You look around the room you are in, it is wooden, unremarkable, \n'
          'and dirty, there is a door leading out of the room to your left \n'
          'and a window to your right \n'
          ' ')
    time.sleep(2)

def first_step():
    print('You stand up, what do you want to, open the door(1), go look out \n' 
          'the window or search the room? Please choose 1, 2 or 3.')
    action = ''
    while action != '1' and action != '2' and action != '3':
        print('Please choose 1, 2 or 3')
        action = input()
        if action == '1':
            print('You open the door, you see that you are in a forest and you \n'
                  'step outside for a better look and realise you were in a wood \n'
                  'cabin, there is an axe leaning against the cabin and you pick \n'
                  'it up as it may be useful')
        elif action == '2':
            print('You go to the window, you see you are in a forest, you notice \n' 
                  'a knife by the window, it might prove useful so you take it')
        elif action == '3':
            print('You search the room, in a drawer you find some money, 10 gold \n' 
                  'coins of some sort')


start_intro()

first_step()

