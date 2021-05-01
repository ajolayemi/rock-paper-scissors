#!/usr/bin/env python
import random
from typing import Any
RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}


def relationship_builder(user_option: list, chosen_option: Any):
    index_of_chosen = user_option.index(chosen_option)
    if chosen_option != user_option[-1]:
        new_list = user_option[index_of_chosen + 1:]

        for preceding in user_option[:index_of_chosen]:
            new_list.append(preceding)
    else:
        new_list = user_option[:index_of_chosen]
    return new_list


def score_getter(player_name):
    with open('rating.txt') as file:
        all_records = file.read().splitlines()
        user_score = list(filter(lambda x: x.split(' ')[0] == player_name, all_records))
        if user_score:
            return int(user_score[0].split(' ')[1])
        else:
            return 0


def game_player():
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    user_score = score_getter(user_name)
    playing_options = input().split(',')
    if playing_options[0] != '':
        weapons = playing_options
    else:
        weapons = list(RULES.keys())

    print("Okay, let's start")

    while True:
        user_weapon = input()
        random_computer_weapon = random.choice(weapons)
        if user_weapon == '!exit':
            print('Bye')
            break
        if user_weapon == '!rating':
            print(f'Your rating: {user_score}')

        elif user_weapon not in weapons:
            print('Invalid input')

        else:

            winning_weapons = relationship_builder(weapons, user_weapon)

            if user_weapon == random_computer_weapon:
                print(f'There is a draw ({user_weapon})')
                user_score += 50

            elif random_computer_weapon in winning_weapons[len(winning_weapons) // 2:]:
                print(f'Well done. The computer chose {random_computer_weapon} and failed')
                user_score += 100
            else:
                print(f'Sorry, but the computer chose {random_computer_weapon}')


if __name__ == '__main__':
    game_player()
