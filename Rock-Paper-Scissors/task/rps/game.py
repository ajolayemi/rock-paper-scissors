#!/usr/bin/env python
import random

RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}


def score_getter(player_name):
    with open('rating.txt') as file:
        all_records = file.read().splitlines()
        user_score = list(filter(lambda x:x.split(' ')[0] == player_name, all_records))
        if user_score:
            return int(user_score[0].split(' ')[1])
        else:
            return 0


def game_player():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    user_score = score_getter(user_name)
    while True:
        user_weapon = input()
        random_computer_weapon = random.choice(list(RULES.keys()))
        if user_weapon == '!exit':
            print('Bye')
            break
        if user_weapon == '!rating':
            print(f'Your rating: {user_score}')

        elif user_weapon not in RULES.keys():
            print('Invalid input')

        elif user_weapon == random_computer_weapon:
            print(f'There is a draw ({user_weapon})')
            user_score += 50
        elif RULES.get(user_weapon) == random_computer_weapon:
            print(f'Well done. The computer chose {random_computer_weapon} and failed')
            user_score += 100
        else:
            print(f'Sorry, but the computer chose {random_computer_weapon}')


if __name__ == '__main__':
    game_player()
