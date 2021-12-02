import random

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def create(num):
    response = []
    for i in range(num):
        response.append(make_response())
    return response


def make_response():
    cipher_text, cipher_ords = make_cipher_text()
    key, key_ords = make_key(random.randint(1, 3))
    message = make_message(key_ords, cipher_ords)

    return {
        'message': message,
        'key': key,
        'cipherText': cipher_text
    }


def make_cipher_text():
    length = random.randint(1, 50)
    cipher_numbers = []
    cipher_text = ''
    for _ in range(length):
        char = random.randint(65, 90)
        cipher_numbers.append(char - 65)
        cipher_text += chr(char)
    return cipher_text, cipher_numbers


def make_key(words=5):
    sentence = []
    sentence_numbers = []
    for i in range(words):
        word = ''
        letters = random.randint(1, 7)
        for j in range(letters):
            letter = get_random_letter()
            word += letter
            sentence_numbers.append(ord(letter.lower()) - 97)
        sentence.append(word)
    return ' '.join(sentence), sentence_numbers


def get_random_letter():
    number = random.randint(0, 51)
    return alphabet[number]


def make_message(key: list[int], c_t: list[int]):
    message = ''
    addition = (65, 97)
    for index, num in enumerate(c_t):
        u_l = random.randint(0, 1)
        space = random.randint(1, 4)
        message += chr((num - key[index % len(key)]) % 26 + addition[u_l])
        if space == 1:
            message += ' '

    return message
