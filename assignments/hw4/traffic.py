"""
Erin Phillips
traffic.py

Problem: This program analyzes traffic patterns.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    roads = eval(input("How many roads were surveyed? "))
    acc1 = 0
    avg = 0
    total_avg = 0
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        acc2 = 0

        for _ in range(days):
            cars = eval(input("How many cars traveled on day " + str(_ + 1) + " ? "))
            acc2 = acc2 + cars
            avg = acc2 / days

        acc1 = acc1 + acc2
        total_avg = acc1 / roads

        print("Road " + str(i + 1) + " average vehicles per day: ", round(avg, 2))

    print("Total number of vehicles travelled on all roads: ", acc1)
    print("Average number of vehicles per road: ", round(total_avg, 2))


if __name__ == '__main__':
    main()
