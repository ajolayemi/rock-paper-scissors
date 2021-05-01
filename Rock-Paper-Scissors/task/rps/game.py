#!/usr/bin/env python

RULES = {'rock': 'scissors',
         'paper': 'rock',
         'scissors': 'paper'}

if __name__ == '__main__':
    user_weapon = input()
    computer_weapon = list(filter(lambda x: RULES[x] == user_weapon, RULES.keys()))[0]
    print(f'Sorry, but the computer chose {computer_weapon}')
