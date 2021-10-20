"""
Name: Erin Phillips
lab8.py
"""

from encode import encode, encode_better


def main():
    number_words('walrus.txt', 'new_walrus.txt')
    hourly_wages('emp_info.txt', 'emp_info_new.txt')
    print(calc_check_sum('0072946520'))
    send_message('message.txt', 'Jeremy')
    send_safe_message('message.txt', 'Hunter', 3)
    send_uncrackable_message('message.txt', 'Bob', 'pad.txt')
    pass


def number_words(in_file, out_file):
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
    i = 1
    for line in in_file:
        new_line = line.split()
        for word in new_line:
            out_file.write(str(i) + ' ' + word + '\n')
            i += 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file, out_file):
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
    for line in in_file:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        out_file.write((' '.join(new_line) + '\n'))
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    add = 0
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10 - i)
        add = add + num
    return add % 11


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    for line in in_file:
        out_file.write(line + '\n')
    in_file.close()
    out_file.close()


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    for line in in_file:
        new_line = encode(line, key)
        out_file.write(new_line + '\n')
    in_file.close()
    out_file.close()


def send_uncrackable_message(file, friend, pad):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    key = open(pad, 'r')
    for line in in_file:
        new_line = encode_better(line, key.readline())
        out_file.write(new_line + '\n')
    in_file.close()
    out_file.close()


main()
