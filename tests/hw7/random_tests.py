import random

first_names = ['Max', 'Ricky', 'Danny', 'Terry', 'Mikey', 'Davey', 'Timmy', 'Tommy', 'Joey', 'Lucky', 'Jem', 'Philip',
               'Willy', 'Vicky', 'Natalie', 'Jean', 'Briana', 'Fran', 'Juliette', 'Greta', 'Andrea', 'Marta', 'Janell',
               'Alicia', 'Kris', 'Ellie']
last_names = ['Crowell', 'Anilkumar', 'Dobson', 'Davidson', 'Harsen', 'Flaherty', 'Shepard', 'Adda', 'Bodine', 'Cristo',
              'Thomson', 'Trammell', 'Kabinov']
middle_names = ['Finley ', '', 'Peyton ', '', 'K. ', '', 'Kerry ', '', 'A. ', '', 'Kendall ', '', 'Jaime ']


def get_random_name():
    first_index = random.randint(0, len(first_names) - 1)
    last_index = random.randint(0, len(last_names) - 1)
    middle_index = random.randint(0, len(middle_names) - 1)

    return f'{first_names[first_index]} {middle_names[middle_index]}{last_names[last_index]}'


def get_test_data():
    names = ['james p hook']
    data = [[100, 80]]
    totals = [(100, 80, 80.0)]
    number_of_students = random.randint(1, 10)

    for i in range(number_of_students):
        name = get_random_name()
        number_of_tests = random.randint(1, 10)
        results = []
        weight = 100
        w_t = 0
        g_t = 0
        a_t = 0

        # getting random weights and grades for each student
        for j in range(number_of_tests):
            random_weight = random.randint(0, weight - 1)
            if j == number_of_tests - 1:
                odds = random.randint(0, 7)
                if odds == 0:
                    random_weight = random.randint(weight, 100)  # if it's 0, the weights will be over
                elif not odds == 1:
                    random_weight = weight  # if it's 1 the weights will be under, otherwise it will be 100
            weight -= random_weight
            grade = random.randint(0, 100)
            w_t += random_weight
            g_t += grade
            a_t += grade * random_weight
            results += [random_weight, grade]
        names.append(name)
        data.append(results)
        totals.append((w_t, g_t, a_t / 100))
    return names, data, totals


def get_expected_values(names, totals):
    class_total = []
    expected_values = []
    for i, name in enumerate(names):
        weight_total, grade_total, avg = totals[i]
        if weight_total == 100:
            expected_values.append(f"{name}'s average: {round(avg, 1)}")
            class_total.append(avg)
        elif weight_total < 100:
            expected_values.append(f"{name}'s average: Error: The weights are less than 100.")
        else:
            expected_values.append(f"{name}'s average: Error: The weights are more than 100.")
    class_average = 0
    if len(class_total) > 0:
        class_average = round(sum(class_total) / len(class_total), 1)
    expected_values.append(f'Class average: {class_average}')
    return expected_values


def create(number=1):
    response = []
    for i in range(number):
        names, data, totals = get_test_data()
        expected_values = get_expected_values(names, totals)
        test_data = []
        for index, name in enumerate(names):
            test_data.append(f'{name}: {" ".join(map(str, data[index]))}')
        response.append({'testData': test_data, 'expectedValues': expected_values})
    return response
