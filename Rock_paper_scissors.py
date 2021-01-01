# Rock, Paper, Scissors

import random

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']

player_move = input("Your move: ")
computer_move = random.choice(moves)
print("You: ", player_move)
print("Me: ", computer_move)

if player_move == computer_move:
    print("Tie")
elif player_move + computer_move in player_wins:
    print("You Win!")
else:
    print("You Lose!")
