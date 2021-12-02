import random


def create(num):
    data = []
    res = []
    for i in range(num):
        monthly_interest = random.uniform(1, 1000)
        monthly_interest_rate = random.uniform(0.00084, 0.08)
        balance_payment_days = monthly_interest / monthly_interest_rate
        monthly_interest_two = round(monthly_interest, 2)
        res.append(monthly_interest_two)
        days = random.randint(1, 31)
        balance_payment = balance_payment_days * days
        payment_days = random.randint(1, 1000)
        balance_days = balance_payment + payment_days
        day_options = list(range(1, 32))
        day_options.remove(days)
        payment_day = random.choice(day_options)
        payment = payment_days / (days - payment_day)
        previous_balance = balance_days / days
        data.append({'rate': monthly_interest_rate * 1200, 'days': days, 'previousBalance': previous_balance,
                     'payment': payment,
                     'paymentDay': payment_day})
    return {'data': data, 'res': res}
