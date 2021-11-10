"""
Erin Phillips
lab11.py
"""

from random import randint


def get_words(word_file):
    file = open(word_file, 'r')
    words = []
    for line in file:
        words.append(line.strip())
    return words


def pick_word(words):
    return words[randint(0, len(words))]


def guess_word(secret_word, guessed_letters, guessed_word, letter):
    check = False
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            guessed_word[i] = letter
            check = True
    if check:
        return True
    guessed_letters.append(letter)
    return False


def word_spelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False


def guess_letter(guessed_letters, secret_word, guessed_word):
    letter = input("Guess a letter: ")
    check = False
    while not check:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("Invalid letter, Try again!")
                letter = input("Guess a letter: ")
                check = False
    if guess_word(secret_word, guessed_letters, guessed_word, letter):
        return True
    else:
        return False


def print_board(guessed_word, turn_count, guessed_letters):
    print("__" + "_____" * len(guessed_word))
    print(guessed_word)
    print("__" + "_____" * len(guessed_word))
    print("Number of Guesses: ", turn_count)
    print("Guessed Letters: ", guessed_letters)
    print()


def play():
    secret_word = pick_word(get_words("word_list.txt"))
    guessed_word = ["_"] * (len(secret_word))
    guessed_letters = []
    turn_count = 0
    print_board(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not word_spelled(guessed_word, secret_word):
        if not guess_letter(guessed_letters, secret_word, guessed_word):
            turn_count += 1
        print_board(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print_board(guessed_word, turn_count, guessed_letters)
        print("Game Over! Better luck next time!")
    else:
        print("Congrats! You won the game!")


def main():
    play()
    pass


main()
