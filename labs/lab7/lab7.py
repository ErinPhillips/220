"""
Name: Erin Phillips
lab7.py
"""


from math import pi


def cash_conversion():
    x = eval(input("Enter an integer: "))
    print("${:.2f}".format(x))


def encode():
    message = input("Enter a word to encode: ")
    key = eval(input("Enter an integer: "))
    acc = " "
    for c in message:
        acc = acc + chr(ord(c) + key)
    print(acc)


def sphere_area(radius):
    return 4 * pi * radius ** 2


def sphere_volume(radius):
    return (4 / 3) * pi * radius ** 3


def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3
    return acc


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    acc = " "
    for i in range(len(message)):
        c = ord(message[i])
        k = ord(key[i % len(key)]) - 97
        acc = acc + chr(c + k)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(3))
    print(sphere_volume(2))
    print(sum_n(5))
    print(sum_n_cubes(7))
    encode_better()


main()
