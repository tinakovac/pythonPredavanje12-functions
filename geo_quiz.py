### A local gaming company contacted you to build a game for them. It is a simple geography quiz where a user has to guess the capital city of some country:

import random

countries_cities = [
{
    "name": "Austria",
    "capital": "Vienna"
}, {
    "name": "Croatia",
    "capital": "Zagreb"
}, {
    "name": "Spain",
    "capital": "Madrid"
}, {
    "name": "Slovenia",
    "capital": "Ljubljana"
}]

restart = True
while restart:
    random.shuffle(countries_cities)
    wrong = 0
    correct = 0
    print("""===============WELCOME=====================""")

    question = input("Would you like to play a game? [y/n]")
    if question == "n":
        restart = False
        print("------------------------------------------")

    if question == "y":
        print("OKAY, Let Start the game. This game is all about guessing the capital of the state. good luck!")
        for state in (countries_cities[:6]):
            question = input("What is the capital of " + state["name"]+ "? ")
            if question != state["capital"]:
                wrong = wrong + 1
                print("That is not correct...")
            if question == state["capital"]:
                correct = correct + 1
                print("That is correct.")
        print("GAME OVER you have ", correct,  "correct and ",(wrong), "wrong" )
        question = input("Do you want to play again? [y/n]")
        if question == "y":
            restart = True
        if question == "n":
            print("Thank you for playing.")
            restart = False
