"""
Name: Erin Phillips
button.py

Problem: this program defines a button class

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import Text


class Button:

    def __init__(self, shape, text):
        """
        Creates a rectangular button with a label
        eg. Button(Rectangle(Point(x, y), Point(x, y)), "button")
        """
        self.shape = shape
        self.text = Text(shape.getCenter(), text)

    def get_label(self):
        """
        Returns the label string of this button
        """
        return self.text.getText()

    def draw(self, win):
        """
        Draws this button and label
        """
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        """
        Un-draws this button and label
        """
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        """
        Returns true if click point is inside this button
        """
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        return (p1.getX() <= point.getX() <= p2.getX() and
                p1.getY() <= point.getY() <= p2.getY())

    def color_button(self, color):
        """
        Sets the color of this button
        """
        self.shape.setFill(color)

    def set_label(self, label):
        """
        Sets the label string of this button
        """
        self.text.setText(label)
