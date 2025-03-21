import random
games = []
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

game_name_dict={
   0 : 0+0,
   1 : 'guess_num',
   2 : 'HangMan',
   3 : 'TruthLie',
   4 : 'ConnectFour',
   5 : 'WordChain',
   6 : 'Unscramble'
}
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
def take_games(extra_text=''):
    global games
    try:
        user_input = input(a+extra_text).strip().lower()
        if user_input == 'r':
            games = random_selection()
        else:
            games = list(eval(user_input))
            for i in range(len(games)):
                games[i] = int(games[i]) 
    except:
         take_games('Invalid pls retype it again>')   
take_games()
print(games,'hello')