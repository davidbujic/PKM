from random import randint
from time import sleep

options = ["PAPIR", "KAMEN", "MAKAZE"]
lose = "Ti si izgubio!"
win = "Ti si pobedio!"

def winner(user_choice, computer_choice):
    print ("%s") % user_choice
    print "Kompjuter bira..."
    sleep(1)
    print ("%s") % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = \
    options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print "Partija je izjednacena!"
        play_RPS()
    elif user_choice_index == 0 and computer_choice_index == 2:
        print win
    elif user_choice_index == 1 and computer_choice_index == 0:
        print win
    elif user_choice_index == 2 and computer_choice_index == 1:
        print win
    elif user_choice_index > 2:
        print "Vasa opcija ne treba da bude veca od 2."
        return
    else:
        print lose
def play_RPS():
    print "Papir, Kamen, Makaze!"
    user_choice = raw_input("Izaberite vasu opciju: ")
    sleep(1)
    user_choice = user_choice.upper()
    computer_choice = options[randint(0,len(options) - 1)]
    winner(user_choice, computer_choice)
play_RPS()
