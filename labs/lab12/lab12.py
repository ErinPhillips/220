"""
Name: Erin Phillips
lab 12.py
"""

from random import randint


def find_and_remove(a_list, value):
    try:
        i = a_list.index(value)
        a_list[i] = "Erin"
    except:
        pass
    return a_list


def read_data(filename):
    f = open(filename, "r")
    file = f.readline()
    file = file.split(" ")
    i = 0
    while i < len(file):
        file[i] = int(file[i])
        i += 1
    return file


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter a number between 1 and 10: "))
    while x < 1 or x > 10:
        x = eval(input("Error! Input out of range \n Enter a number between 1 and 10: "))
    return x


def num_digits():
    x = eval(input("Enter a positive integer: "))
    while x > 0:
        y = 0
        while x != 0:
            y += 1
            x //= 10
        print("Number of digits = ", y)
        x = eval(input("Enter a positive integer: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("Guess a number between 1 and 100:"))
    while guesses < 7 and guess != num:
        if guess > num and guess != 6:
            guess = eval(input("Too high! Guess again! "))
        elif guess < num and guess != 6:
            guess = eval(input("Too low! Guess again! "))
        guesses += 1
    if guess == num:
        print("Congrats! You win in", guesses, "guesses!")
    else:
        print("Oh no! You lost. The number was", num, "!")


def main():
    a_list = [1, 2, 3, 4, 5, 6]
    print(find_and_remove(a_list, 2))
    print(read_data("data_sorted.txt"))
    print(is_in_linear(70, read_data("data_sorted.txt")))
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
