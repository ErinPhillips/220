from random import randint

from .test_case import TestCase, Road


def create(number, total_roads_needed):
    # always test this case, so total test cases are number + this one
    test_cases = [TestCase([Road(1, [0])])]

    roads_per_test_case = [0] * number
    for n in range(total_roads_needed):
        roads_per_test_case[n % number] += 1

    # [3, 3, 2]
    for num_roads in roads_per_test_case:
        roads = []
        for road_number in range(num_roads):
            number_of_days = randint(1, 10)
            cars_per_day = []
            for day in range(number_of_days):
                cars_per_day.append(randint(1, 50))
            road = Road(road_number + 1, cars_per_day)
            roads.append(road)

        test_cases.append(TestCase(roads))

    return test_cases
