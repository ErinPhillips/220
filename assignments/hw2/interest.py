"""
Name: Erin Phillips
interest.py

Problem: This program computes the monthly interest charge on a credit card.

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""


def main():
    rate = eval(input("Enter the annual interest rate: "))
    days = eval(input("Enter the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter the previous balance: "))
    payment = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day of the billing cycle the payment was made: "))
    end = days - payment_day
    avg_daily_balance = ((previous_balance * days) - (payment * end)) / days
    monthly_rate = rate/(12*100)
    monthly_charge = avg_daily_balance * monthly_rate
    print(round(monthly_charge, 2))


if __name__ == '__main__':
    main()
