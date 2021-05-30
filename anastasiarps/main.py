import random
import time
from lib import hierarchy
from tkinter import *

root = Tk()

def mcall():
    rps = random.randint(1, 3)
    motto = ["Rock", "Paper", "Scissors", "Shoot"]

    answer = input("Please Select a move: 1.) Rock, 2.) Paper, 3.) Scissors: ")
    if (answer == "1" or answer == "1.)" or answer.lower == "rock"):
        move = 1

    elif (answer == "2" or answer == "2.)" or answer.lower == 'paper'):
        move = 2

    elif (answer == '3' or answer == '3.)' or answer.lower == 'scissors'):
        move = 3
    for words in motto:
        time.sleep(0.5)
        print(words)

    hierarchy.compare(move, rps)
    contnu = 'true'
    while(contnu == "true"):
        playAgain = input("Would you like to play again?: y/n?")

        if (playAgain == "y" or playAgain == "yes"):
            contnu = "true"
            mcall()
        else:
            contnu = "false"


mcall()