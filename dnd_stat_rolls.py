import random as r
import csv


RACES = []
CLASSES = []

with open('data/classes.csv', 'r') as file:
    for item in file:
        CLASSES.append(item)

with open('data/races.csv', 'r') as file:
    for item in file:
        RACES.append(item)


def character_creation_rolls():
    roll_holding_list = []
    stat_holding_list = []
    for i in range(1, 7):
        for i in range(1, 5):
            roll_holding_list.append(r.randint(1, 6))
        roll_holding_list.sort(reverse=True)
        roll_holding_list.pop()
        roll = sum(roll_holding_list)
        stat_holding_list.append(roll)
        roll = 0
        roll_holding_list = []
    stat_holding_list.sort(reverse=True)
    return stat_holding_list


def character_class_roll():
    return str(r.choice(CLASSES)).strip()


def character_race_roll():
    return str(r.choice(RACES)).strip()


def character_alignment_roll():
    pass


def print_character(character=None):
    if character == None:
        character_stats = character_creation_rolls()
        for stat in character_stats:
            print(stat)

        print('-------------')
        character_race = character_race_roll()
        character_class = character_class_roll()
        print(character_alignment)
        print(character_race + ' - ' + character_class)
    else:
        for stat in character:
            print(stat)

        print('-------------')
        character_race = character_race_roll()
        character_class = character_class_roll()
        print(character_alignment)
        print(character_race + ' - ' + character_class)


def generate_one_good_one_bad_character():
    counter = 0
    best_character = []
    worst_character = [18, 18, 18, 18, 18, 18]
    while counter < 10000:
        counter += 1
        character_stats = character_creation_rolls()
        if sum(character_stats) > sum(best_character):
            best_character = character_stats
        if sum(character_stats) < sum(worst_character):
            worst_character = character_stats

    print('Best Character')
    print_character(best_character)
    print('Worst Character')
    print_character(worst_character)


if __name__ == "__main__":
    print_character()
