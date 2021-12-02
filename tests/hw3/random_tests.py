import random
import math
from functools import reduce


def make_test_data(num):
    data = []
    for i in range(0, num):
        nums = random.randint(1, 15)
        set_nums = []
        for i in range(0, nums):
            set_nums.append(random.randint(1, 100))
        data.append(set_nums)
    return data


def create(number):
    test_data = make_test_data(number)
    res = []
    for data_set in test_data:
        res.append(
            (
                round(math.sqrt(reduce(lambda x, y: x + y * y, data_set, 0) / len(data_set)), 3),
                round(math.pow(reduce(lambda x, y: x * y, data_set, 1), 1 / len(data_set)), 3),
                round(len(data_set) / reduce(lambda x, y: x + 1 / y, data_set, 0), 3)
            )
        )

    r = map(lambda a: {'rmsAvg': a[0], 'geometricMean': a[1], 'harmonicMean': a[2]}, res)

    return {'data': test_data, 'answers': list(r)}
