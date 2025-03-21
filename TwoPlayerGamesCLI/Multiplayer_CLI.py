player1_points = []
player2_points = []
p1_total = 0
p2_total =0
games = []
reactions = ["⚆_⚆", "🫡", "😊", "😁", "😀", "😎", "🤨", ";D", "(⓿_⓿)", "^_^", "><", "(^_^)", "⊙﹏⊙∥"]
from TwoPlayerGamesCLI import guess_num

import os
from TwoPlayerGamesCLI import TruthLie 
from TwoPlayerGamesCLI import WordChain
from TwoPlayerGamesCLI import Unscramble
from TwoPlayerGamesCLI import ConnectFour
from TwoPlayerGamesCLI import HangMan
import random
a = '''
Pls select your games . 
You may select as many games as you like. 

Format:
Enter the game numbers in the form of a list.
[1,5,3,1]

note:
you can type the number repeatedly for playing the same game game over
only int game numbers are accepted


Games:
1) Number guessing 🔢
2) Hang man 😵
3) 2 truths and a lie 🤫
4) coonect 4 (⓿_⓿)
5) word chain ⛓️
6) scramble unscramble word 🧠

Type: r if you want the games to be randomly selected
>'''
Game_call_codes={
   0 : 0+0,
   1 : guess_num.main_game,
   2 : HangMan.hangman_game,
   3 : TruthLie.game,
   4 : ConnectFour.play_game,
   5 : WordChain.word_chain_game,
   6 : Unscramble.scrambled_word_game
}
game_name_dict={
   0 : 0+0,
   1 : 'guess_num',
   2 : 'HangMan',
   3 : 'TruthLie',
   4 : 'ConnectFour',
   5 : 'WordChain',
   6 : 'Unscramble'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_selection():
    game_list = []
    try:
        num_games=int(input('Pls input the number of games you want. >>>'))
    except:
        print('Pls enter an integer value')
        random_selection()
    print("The following games are selected:")
    count = 0
    for i in range(num_games):
        count += 1
        _game_code = random.randint(1,6)
        game_list.append(_game_code)
        print(f'{count}. {game_name_dict.get(_game_code,"ERROR")}')
    return game_list

def take_games(extra_text=''):
    global games
    try:
        user_input = input(a+extra_text).strip().lower()
        if 'r' in user_input:
            games = random_selection()
        else:
            games = list(eval(user_input))
            for i in range(len(games)):
                games[i] = int(games[i]) 
    except:
         take_games('Invalid pls retype it again>')   
    input("Press enter to start the games") 
    clear_screen()

def output_marks():
    global p1_total, p2_total
    score_variancy = p1_total - p2_total
    winner = 'Player1' if score_variancy > 0 else 'Player2' if score_variancy < 0 else 'Draw'
    print(f'''
Player 1 | total = {p1_total} | marks spectator = {player1_points}
Player 2 | total = {p2_total} | marks spectator = {player2_points}''')
    if winner == 'Draw':
        print("It's a Draw 😅")
    else:
        print(f'{winner} wins by {abs(score_variancy)} points.')
    count = 0
    print("These were the games:")
    for i in range(len(games)):
        count += 1
        print(f'{count}. {game_name_dict.get(games[i],'Error')}')

def appending_points(mytuple=(0,0)):
    global p1_total, p2_total
    p1,p2 = mytuple
    player1_points.append(p1)
    player2_points.append(p2)
    p1_total += p1
    p2_total += p2
    print(f'''
Player 1 | total = {p1_total} | marks gained = {p1}
Player 2 | total = {p2_total} | marks gained = {p2}
''')


def next_game():
    print(reactions[random.randint(0,len(reactions)-1)])
    print('Press enter to start the next game')
    input('>')
    clear_screen()
    

def main():
    take_games()
    for v in range(len(games)):
        appending_points(Game_call_codes.get(games[v], lambda: (0,0))())
        try:
            print(f'The next game is :{game_name_dict.get(games[v+1],lambda :(0+0))}')
            next_game()
        except:
            print('The games are finished')
            input('press enter to see the scores')
            clear_screen()
        
    output_marks()
    x = input('Press enter to leave')

