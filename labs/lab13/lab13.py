"""
Name: Erin Phillips
lab13.py
"""


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


def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        item = values[mid]
        if search_val == item:
            return True
        if search_val < item:
            high = mid - 1
        else:
            low = mid + 1
    return False


def selection_sort(values):
    for i in range(len(values)):
        low = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < low:
                low = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def get_area(rect):
    p1, p2 = rect.getP1(), rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w * h


def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]


def trade_alert(filename):
    file = open(filename, 'r')
    data = file.read().split()
    i = 0
    while i < len(data):
        sec = i + 1
        if float(data[i]) > 830:
            print("ALERT: Trading volume exceeds 830 at", sec, "seconds!")
        if 500 < float(data[i]) < 830:
            print("WARNING: Trading volume exceeds 500 at", sec, "seconds!")
        i += 1


def main():
    trade_alert("trades.txt")
    pass


main()
