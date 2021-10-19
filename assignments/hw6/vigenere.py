"""
Erin Phillips
vigenere.py

Problem: This program encodes a message using a Vigenere cipher

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Point, Entry, Rectangle


def prompt(point, message, win):
    txt = Text(point, message)
    txt.draw(win)


def button(win):
    encode_box = Rectangle(Point(8, 5), Point(12, 9)).draw(win)
    encode_text = Text(Point(10, 7), 'Encode').draw(win)
    win.getMouse()
    encode_box.undraw()
    encode_text.undraw()


def code(message, keyword):
    m = message.upper().replace(" ", "")
    k = keyword.upper()
    cipher_text = ""
    for i in range(len(m)):
        m_ord = ord(m[i]) - 65
        k_ord = ord(k[i % len(k)]) - 65
        new_message = 65 + (m_ord + k_ord) % 26
        cipher_text += chr(new_message)
    return cipher_text


def main():
    win = GraphWin('Vigenere', 500, 300)
    win.setCoords(0, 0, 20, 20)

    # Entry
    prompt(Point(4, 16), 'Message to code', win)
    prompt(Point(4, 13), 'Enter Keyword', win)
    k_entry = Entry(Point(10, 13), 15).draw(win)
    m_entry = Entry(Point(13, 16), 30).draw(win)

    # Encode button
    button(win)

    # Encode output
    message = m_entry.getText()
    key = k_entry.getText()

    prompt(Point(10, 5), code(message, key), win)
    prompt(Point(10, 8), 'Resulting Message:', win)
    prompt(Point(10, 1), 'Click anywhere to close.', win)

    win.getMouse()


main()
