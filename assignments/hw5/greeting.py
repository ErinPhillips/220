"""
Erin Phillips
greeting.py

Problem: This displays a greeting card for Valentines Day.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

import time
import graphics as g


def main():
    win = g.GraphWin("Greeting Card", 600, 600)
    win.setCoords(0, 0, 20, 20)
    win.setBackground('light pink')

    # envelope and greeting
    letter = g.Rectangle(g.Point(4, 16), g.Point(16, 8))
    envelope = g.Polygon(g.Point(2, 16), g.Point(10,12), g.Point(18, 16),
                         g.Point(18, 6), g.Point(2, 6))
    envelope2 = g.Polygon(g.Point(2, 16), g.Point(10, 12), g.Point(18, 16),
                          g.Point(10, 20), g.Point(2, 16))
    letter.setFill('white')
    envelope.setFill('dark red')
    envelope2.setFill('dark red')

    prompt_text = g.Text(g.Point(10, 10), "You've got mail!")
    prompt_text.setSize(35)
    prompt_text.setFill('light blue')
    prompt_text2 = g.Text(g.Point(10, 2), "Click to open!")
    prompt_text2.setSize(35)
    prompt_text2.setFill('dark red')

    envelope2.draw(win)
    letter.draw(win)
    envelope.draw(win)
    prompt_text.draw(win)
    prompt_text2.draw(win)

    win.getMouse()

    # move letter
    for _ in range(20):
        letter.move(0, 1)
        time.sleep(0.1)

    envelope.undraw()
    envelope2.undraw()
    letter.undraw()
    prompt_text.undraw()
    prompt_text2.undraw()

    # heart
    heart1 = g.Circle(g.Point(7, 12), 3)
    heart2 = heart1.clone()
    heart2.move(5.75, 0)
    heart3 = g.Polygon(g.Point(10, 12), g.Point(5, 9.75), g.Point(10, 5), g.Point(14.75, 9.75))
    arrow_stop = g.Polygon(g.Point(10, 12), g.Point(10, 5), g.Point(14.75, 9.75))

    heart1.setFill('dark red')
    heart2.setFill('dark red')
    heart3.setFill('dark red')
    heart1.setOutline('dark red')
    heart2.setOutline('dark red')
    heart3.setOutline('dark red')
    arrow_stop.setOutline('dark red')

    heart1.draw(win)
    heart3.draw(win)

    # arrow and tail
    arrow = g.Line(g.Point(1, 2), g.Point(4, 5))
    l_arrow_tail = g.Line(g.Point(.5, 2), g.Point(1, 2))
    r_arrow_tail = g.Line(g.Point(1, 2), g.Point(1, 1.5))

    arrow.setArrow('last')
    arrow.setWidth(3)

    arrow.setFill('yellow')
    l_arrow_tail.setFill('yellow')
    r_arrow_tail.setFill('yellow')

    arrow.draw(win)
    l_arrow_tail.draw(win)
    r_arrow_tail.draw(win)
    heart2.draw(win)
    arrow_stop.draw(win)

    # move arrow and tail
    for _ in range(20):
        arrow.move(1, 1)
        l_arrow_tail.move(1, 1)
        r_arrow_tail.move(1, 1)

        time.sleep(0.1)

    # final message
    message = g.Text(g.Point(10, 18), 'Happy Valentines Day! ')
    prompt_text2.setText('Click anywhere to close!')
    prompt_text.setText("BE \n MINE ")

    message.setSize(20)
    prompt_text2.setSize(20)

    message.setFill('dark red')

    message.draw(win)
    prompt_text.draw(win)
    prompt_text2.draw(win)

    win.getMouse()


if __name__ == '__main__':
    main()
