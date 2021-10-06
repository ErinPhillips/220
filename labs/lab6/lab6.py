"""
Erin Phillips
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter your first and last name in the format First-Last: ")
    split_name = name.split('-')
    print(split_name[1] + str(', ') + split_name[0])


def company_name():
    domain_name = input("Please enter the three-part internet domain name \n"
                        "using the format www.example.com: ")
    company = domain_name.split('.')
    print(company[1])


def initials():
    num = eval(input("How many names will be input? "))
    for i in range(num):
        first_name = input("Enter the first name of student " + str(i + 1) + ": ")
        last_name = input("Enter " + str(first_name) + "'s last name: ")
        print(first_name[0] + last_name[0])


def names():
    x = input("Enter people's first and last names, separated by commas: ")
    name = x.split(", ")
    for name in name:
        initial = name.split(" ")
        print(initial[0][0] + initial[1][0], end=" ")
    print()


def thirds():
    num = eval(input("How many sentences will be input? "))
    for i in range(num):
        sentence = input("Enter sentence " + str(i+1) + ": ")
        print(sentence[2::3])


def word_average():
    x = input("Enter a sentence: ")
    acc = 0
    words = x.split()
    for word in words:
        acc = acc + len(word)
    print(acc / len(words))


def pig_latin():
    phrase = input("Enter a sentence: ").lower()
    words = phrase.split(" ")
    for word in words:
        new_phrase = word[1:] + word[0] + "ay"
        print(new_phrase, end=' ')


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
