from __future__ import division
import time
import sys
import random
from collections import defaultdict
import os

index = defaultdict(list)

def init_words():
    global words
    with open("dictionary.txt") as file:
        for line in file:
            word = line.strip().lower()
            index[len(word)].append(word)


def choose_word(difficulty):
    global words
    temp_word = str(random.choice(words))
    while len(temp_word) != get_word_length(difficulty):
        temp_word = str(random.choice(words))
    return temp_word.lower()


def clear_screen():
    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2":
        # Linux
        os.system('clear')
    elif _platform == "darwin":
        # Mac OS X
        os.system('clear')
    elif _platform == "win32":
        # Windows
        os.system('cls')


def get_word_length(dif):
    return {
        1: 6,
        2: 8,
        3: 10,
        4: 13,
        5: 15
    }[dif]


def insert_logo():
    print """
 _____
/ ____|  WORD
| |  __ _   _  ___  ___ ___
| | |_ | | | |/ _ \\/ __/ __|
| |__| | |_| |  __/\\__ \__ \\
\\_____|\\__,_|\\___||___/___/
         
             By Michael Parker \n"""



def initialize():
    clear_screen()
    insert_logo()
    
    print "Welcome to Word Guess! This game is a simple word guessing game written in Python."
    print "\nPlease read the readme.txt file before playing so you know the rules!"
    print "\nDISCLAIMER: The words used in this game are chosen randomly",
    print "\nfrom the dictionary file named 'dictionary'. It does contain some swear words",
    print "\nand I apologise if you get one of them, out of thousands of words available."

    user_ready = raw_input("\nAre you ready?! (y/n): ").lower().strip()
    if len(user_ready) > 0 and user_ready[0] == "y":

        lets_go = "Let's go!"
        print
        print lets_go + " 3... ",
        sys.stdout.flush()
        time.sleep(1)
        for i in range(2,0, -1):
            print "\r" + lets_go + " " + str(i) + "... ",
            sys.stdout.flush()
            time.sleep(1)

        clear_screen()
        insert_logo()
        return True
    else:
        print "\nOK, come back whenever you're ready!"
        return False



def play_round(difficulty):

    length = int(raw_input("Enter word length: "))
    word = random.choice(index[length])
    
    guessed = []
    wrong = []
    tries = 5
    
    while tries > 0:
    
        out = ""
        
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + " _ "
        
        if out == word:
            break
        
        print("Guess the word:", out)
        print(tries, "chances left")
        
        guess = raw_input()
        
        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Well Done!")
            guessed.append(guess)
        else:
            print("Nope! Try again!")
            tries = tries - 1
            wrong.append(guess)
        
        print()
        
    if tries:
        print("You guessed", word)
    else:
        print("You didn't get", word)
        

def play_game():
    lives = 3
    points = 0
    difficulty = 1

    should_harden = False
    increment_lives = 0

    while lives > 0:

        print "Lives: %s\t\tPoints: %s\t\tDifficulty: %s" % (str(lives), str(points), str(difficulty))

        if points >= 10000:
            print "\nSeriously, who are you?! You know all words in English right?!\nCongrats!!!"
            return
        else:

            print
            won_or_lost = play_round(difficulty)
            print


            if won_or_lost[0] is True:
                print "Nice! You got it right!"
                if difficulty < 5:
                    difficulty += should_harden
                    should_harden = not should_harden
                    increment_lives += 1
                points += won_or_lost[2] * 100

            else:
                print "I see you couldn't get that one?!\nThe right answer was \"" + won_or_lost[1] + '"!'
                lives -= 1

            sys.stdout.flush()
            time.sleep(3)

            if increment_lives == 3:
                lives += 1
                increment_lives = 0

            clear_screen()
            insert_logo()


def main():
    ready_to_play = initialize()
    if ready_to_play is True:

        play_game()

        play_again = raw_input("\nPlay again? (y/n): ").lower().strip()
        
        if len(play_again) > 0 and play_again[0] == "y":
            main()
        else:
            print "\nThanks for playing Word Guess! See you again soon!\n"

init_words()
main()