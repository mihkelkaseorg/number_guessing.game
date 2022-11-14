import random
from time import sleep
game_ended = False


def pick_level():
    level = None
    while not level:
        difficulty = input("Difficulty: ")
        if difficulty == "1":
            level = 3
        elif difficulty == "2":
            level = 5
        elif difficulty == "3":
            level = 10
        else:
            print("wrong option")
    if level:
        start_game(level)


def start_game(level):
    while True:
        computer = random.randint(1, level)
        player = input(f"Guess the computers number from 1 to {level}: ")
        if not player.isnumeric():
            print("invalid option")
            continue
        elif int(player) == computer:
            print(f"Computer says: {computer}, you say: {player}")
            print("You won!")
            while True:
                another_round = input("Play another round? (y/n)")
                if another_round == "y":
                    pick_level()
                elif another_round == "n":
                    print('thanks for playing')
                    sleep(1)
                    exit()
                else:
                    print("Wrong option.")
                    continue
        elif int(player) in range(1, level + 1):
            print(f"Computer says: {computer}, you say: {player}")
            continue
        else:
            print("invalid option")
            continue


while not game_ended:
    print('Welcome to the number guessing game! Please choose the difficulty: '
          'easy - 1; '
          'medium - 2; '
          'hard - 3')
    pick_level()


print('thanks for playing!')