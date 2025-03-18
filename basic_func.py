import os
import keyboard
import Multiplayer_CLI as cli_main
def clear_screen():
    # Check the operating system and clear the terminal accordingly
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Mac
        os.system('clear')

def taking_input(message,_description=None):
    main_message = message
    text = message.lower()
    if text == 'help':
        print('''
you should type (note: <word> = what it does)
description = how to play the game
quit = stop playing or leave the current game
score = to see the current points 
''')
    elif text == 'description':
        if _description is not None:
            _description()
    elif text == 'quit':
        print('Are you sure you want to leave the game')
        print('Type q if you want to stop playing')
        print('Type c if you want to leave the current game only')
        print('Type s if want to continue')
        x = ''
        while True:
            x = input("Enter a character: ").lower().strip()
            if len(x) == 1 and x in ['q', 'c', 'r']:
                break
            print("Invalid input. Please enter a single character, and it must be one of 'q', 'c', or 'r'.")
        if x == 'q':
            print("Program terminated.")
            cli_main.output_marks()
            exit()
        elif x == 'c':
        
    elif text == 'score':
        cli_main.output_marks()
    return main_message
