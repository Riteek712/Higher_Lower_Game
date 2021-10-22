from art import logo, vs
from Data import data
from random import randint
import os

x = len(data) # to find outtotal number of datasets of the celebrities we have.
score_card = 0 # to keep track of score when someone is playing.
game_is_on = True # A condition for the while loop.


def celebrity_1(x):
    #To determine the index of a celebrity 1.
    p1 = randint(1, x)
    return p1


def celebrity_2(i1, x):
    # To determine the index of a celebrity 2.
    p2 = randint(1, x)

    while p2 == i1:
        #this is to make sure the same celebrity doesnt get selected by both functions.
        p2 = randint(1, x)
    return p2

def compare_p1_p2(a, b):

    if a > b:
        return 'l'
    else:
        return 'h'



py_1 = celebrity_1(x)
py_2 = celebrity_2(py_1, x)
print("************************************************************************************************************************")
print(logo)
while game_is_on:

    print("Guess which one of them has more followers!!")

    #print the detailes of first celebrity.
    print(f" \n{data[py_1]['name']} is a {data[py_1]['description']} from {data[py_1]['country']} ...")
    pl_1_followers = data[py_1]['follower_count']

    print(vs)

    # print the detailes of second celebrity.
    print(f"{data[py_2]['name']} is a {data[py_2]['description']} from {data[py_2]['country']} ...")
    pl_2_followers = data[py_2]['follower_count']
    correct_ans = compare_p1_p2(pl_1_followers, pl_2_followers)

    print(f"Does {data[py_2]['name']} has higher or lower number of followers compared to {data[py_1]['name']}!")
    ans = input("Enter 'h' for higher and 'l' for lower: ")

    #to check if the value entered is valid.
    while (ans != 'h') and (ans != 'l'):
        ans = input(" \nINVALID ENTRY!\nEnter the correct codes properly\nEnter 'h' for higher and 'l' for lower: ")

    if ans == correct_ans:
        score_card += 1
        os.system("cls")
        print("************************************************************************************************************************")
        print(logo)
        print(f"CORRECT ANSWERE!!\nYour current score: {score_card}.")

        # Now changing celebrity no.2 to celebrity No.1 and making new celebrity No.2 .
        py_1 = py_2
        py_2 = celebrity_2(py_1, x)

    else:
        game_is_on = False

        if score_card >= 15:
            print(f" \nWOW! Amzing you scored {score_card} points.")
        elif score_card >= 7:
            print(f" \nWell played! You scored {score_card} points. ")
        elif score_card >= 4:
            print(f" \nHard luck buddy! only {score_card} points.")
        elif score_card != 0:
            print(f" \nWOW you really do SUCK!!! only {score_card} points")
        else:
            print(f" \nWell have fun with that BIG {score_card}\n ")

        os.system('cls')
        print("So? want to try yourself again...")
        # Asking the player wheather he/she wants to play a new game.
        try_again = input("Enter 'y' for yes and 'n' for no: " )
        # to check if the value entered is valid.
        while (try_again != 'y') and (try_again != 'n'):
            try_again = input(" \nINVALID ENTRY!\nEnter the correct codes properly\nEnter 'y' for yes and 'n' for no: ")

        if try_again == "y":
            score_card = 0
            py_1 = py_2
            py_2 = celebrity_2(py_1, x)
            game_is_on = True
        else :
            print(" \nThanks for Playing! \nHave a good day!")