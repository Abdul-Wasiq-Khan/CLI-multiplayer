player1_points = []
player2_points = []
p1_total = 0
p2_total =0
games =[]
import guess_num
import basic_func
import TruthLie 
import WordChain
a = '''
Pls select your games . 
you may select as many as you like 

enter it in form of a list 
in the following format
[1,5,3,1]
note only int game number are accepted

Games:
1) Number guessing
2) Hang man
3) Dinosaur🦖
4) dodgeing
5) 2 truths and a lie
6) coonect 4
7) word chain
8) scramble unscramble word
>
'''
def take_games():
    try:
        games = eval(input(a))
        count = 0
        for i in games:
            games[count] = int(i)
            count += 1
    except:
        print('invalid pls retype it')
        take_games()
take_games()

def output_marks():
    score_variancy = p1_total - p2_total
    winner = ''
    if score_variancy > 0:
        winner = 'Player1'
    elif score_variancy < 0:
        winner = 'Player2'
    else:
        winner = 'null'

    print(f'''
Player 1 | total = {p1_total}| marks spectator = {player1_points}
Player 2 | total = {p2_total}| marks spectator = {player2_points}
{winner} wins by {score_variancy}
''')
    
def appending_points(mytuple=(0,0)):
    p1,p2 = mytuple
    player1_points.append(p1)
    player2_points.append(p2)
    p1_total += p1
    p2_total += p2

game_dict={
    0: 0+0,
   1 : guess_num.main_game(),
   5 : TruthLie.game(),
   7 : WordChain.word_chain_game(),
}

for i in games:
    appending_points(eval(game_dict.get(i,0)))


