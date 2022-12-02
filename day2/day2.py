import math

scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

rps_defeats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

rps_wins = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

elf_play = {
    "A": "rock",
    "B": "paper",
    "C": "scissors" 
}

i_play = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

def get_moves(pair):
    return (elf_play[line[0]], i_play[line[1]])

def get_game_score(elf_move, my_move):
    if my_move == rps_defeats[elf_move]:
        return 0
    elif elf_move == rps_defeats[my_move]:
        return 6
    else:
        return 3

#Part 1
with open("./input.txt") as f:
    total = 0
    for line in f:
        line = line.strip()
        line = line.split(" ")
        elf_move, my_move = get_moves(line)
        game_score = get_game_score(elf_move, my_move) + scores[my_move]
        total += game_score
    print(total)



def get_move(letter, elf_move):
    if letter == 'Y':
        return elf_move
    elif letter == 'X':
        return rps_defeats[elf_move]
    else:
        return rps_wins[elf_move]

#Part 2
with open("./input.txt") as f:
    total = 0
    for line in f:
        line = line.strip()
        line = line.split(" ")
        elf_move = elf_play[line[0]] 
        my_move = get_move(line[1], elf_move)
        print((elf_move, my_move))
        game_score = get_game_score(elf_move, my_move) + scores[my_move]
        total += game_score
    print(total)