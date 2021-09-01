"""
Name: <Erin Phillips>
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

calc_area()

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

calc_volume()

def calc_shooting_percentage():
    taken = eval(input("Enter the number of shots taken: "))
    made = eval(input("Enter the number of shots made: "))
    percentage = made / taken * 100
    print("Shooting Percentage =", percentage)

calc_shooting_percentage()

def coffee():
    purchased = eval(input("Enter the number of pounds of coffee purchased: "))
    price_per_pound = 10.5
    shipping_per_pound = 0.86
    fixed_rate = 1.5
    order = price_per_pound * purchased + shipping_per_pound * purchased + fixed_rate
    print("Total Cost =", order)

coffee()

def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers: "))
    miles = kilometers / 1.61
    print ("Miles =", miles)

kilometers_to_miles()

