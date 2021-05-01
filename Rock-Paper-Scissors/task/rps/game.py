#!/usr/bin/env python
import random

RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}


def game_player():
    while True:
        user_weapon = input()
        random_computer_weapon = random.choice(list(RULES.keys()))
        if user_weapon == '!exit':
            print('Bye')
            break
        if user_weapon not in RULES.keys():
            print('Invalid input')

        elif user_weapon == random_computer_weapon:
            print(f'There is a draw ({user_weapon})')
        elif RULES.get(user_weapon) == random_computer_weapon:
            print(f'Well done. The computer chose {random_computer_weapon} and failed')
        else:
            print(f'Sorry, but the computer chose {random_computer_weapon}')


if __name__ == '__main__':
    game_player()
