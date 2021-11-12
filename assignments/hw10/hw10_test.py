import os
import random

from hw10.sales_force import SalesForce
from hw10.sales_person import SalesPerson
from tests.test_framework import *


class TestClass:

    def test_stuff(self):
        test_suit = TestSuit('HW 10')
        sales_person_builder = TestBuilder('Sales Person', 'sales_person.py', 15)
        sales_force_builder = TestBuilder('Sales Force', 'sales_force.py', 16)
        constructor_section, instance_vars_section, methods_section = sales_person_test()
        c, i, m = sales_force_test()

        sales_person_builder.add_items(constructor_section, instance_vars_section, methods_section)
        # sales_person_builder.run()

        sales_force_builder.add_items(c, i, m)
        # sales_force_builder.run()
        test_suit.add_test_builders(sales_person_builder, sales_force_builder)
        test_suit.run()


def make_sales_person_with_sales(sp_id, sp_name, sale_1, sale_2):
    sales_person = SalesPerson(sp_id, sp_name)
    sales_person.enter_sale(sale_1)
    sales_person.enter_sale(sale_2)
    return sales_person


def sales_person_test():
    SALES_PERSON_ID = random.randint(0, 1000)
    SALES_PERSON_NAME = get_random_full_name()

    # Test Constructor
    constructor_section = Section('Constructor')
    outcome, sales_person = run_safe(lambda: SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME))
    if not outcome:
        print('\nFAILED: Could not construct SalesPerson, no more test will run.')
        sys.exit(1)
    constructor_section.add_items(Test('initialize constructor', True, True, show_actual_expected=False))

    # test instance variables
    iv_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    instance_variables_section = Section('Instance Variables')
    employee_id_test = Test('instance variable employee_id', lambda: type(iv_person.employee_id), int)
    name_test = Test('instance variable name', lambda: type(iv_person.name), str)
    sales_test = Test('instance variable sales', lambda: type(iv_person.sales), list)
    instance_variables_section.add_items(employee_id_test, name_test, sales_test)

    # test methods
    methods_section = Section('Methods')
    # get_id
    methods_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    methods_section.add_items(Test('get_id', lambda: methods_person.get_id(), SALES_PERSON_ID))
    # get_name
    methods_section.add_items(Test('get_name', lambda: methods_person.get_name(), SALES_PERSON_NAME))
    # set_name
    new_name = 'New Name'

    set_name_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)

    def set_name_test():
        set_name_person.set_name(new_name)
        return set_name_person.name

    methods_section.add_items(Test('set_name', set_name_test, new_name))
    # enter_sale
    enter_sale_person = SalesPerson(SALES_PERSON_ID, SALES_PERSON_NAME)
    sale_amount_1 = random.uniform(0, 100.00)
    sale_amount_2 = random.uniform(0, 100.00)
    total_sales = sale_amount_1 + sale_amount_2

    def sale_test():
        enter_sale_person.enter_sale(sale_amount_1)
        enter_sale_person.enter_sale(sale_amount_2)
        return enter_sale_person.sales[0], enter_sale_person.sales[1]

    methods_section.add_items(Test('enter_sale', sale_test, (sale_amount_1, sale_amount_2)))

    # total_sales
    methods_section.add_items(Test('total_sales', lambda: enter_sale_person.total_sales(), total_sales))

    # get_sales
    methods_section.add_items(Test('get_sales', lambda: enter_sale_person.get_sales(), [sale_amount_1, sale_amount_2]))

    # met_quota
    try:
        quota_sales_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1,
                                                          sale_amount_2)
        quota_hit = random.uniform(0, total_sales)
        quota_miss = random.uniform(total_sales + 1, total_sales + 1000)
        a = lambda: quota_sales_person.met_quota(quota_hit)
        b = lambda: quota_sales_person.met_quota(quota_miss)

        quota_tests = [(a, True, quota_hit, 'hit'), (b, False, quota_miss, 'miss')]
        for lambda_func, expected, quota, test_type in quota_tests:
            methods_section.add_items(
                Test(f'met_quota - {test_type}', lambda_func, expected,
                     data=[f'quota: {quota}', f'sales amount: {total_sales}']))
    except Exception as e:
        methods_section.add_items(
            Test('met_quota - hit', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]))
        methods_section.add_items(
            Test('met_quota - miss', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]))

    # compare_to
    try:
        compare_to_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1,
                                                         sale_amount_2)
        other_person_equal = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_equal.sales = compare_to_person.sales
        lambda_equal = compare_to_person.compare_to(other_person_equal)

        other_person_greater = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_greater.sales = [sum(compare_to_person.sales) + 1]
        lambda_less_than = compare_to_person.compare_to(other_person_greater)

        other_person_less = SalesPerson(compare_to_person.employee_id, compare_to_person.name)
        other_person_less.sales = [sum(compare_to_person.sales) - 1]
        lambda_greater_than = compare_to_person.compare_to(other_person_less)

        for lambda_func, expected, other, test in (
                (lambda_equal, 0, other_person_equal, 'equal'),
                (lambda_less_than, -1, other_person_greater, 'less than'),
                (lambda_greater_than, 1, other_person_less, 'greater than')):
            methods_section.add_items(Test(f'compare_to - {test}', lambda_func, expected,
                                           data=[f'this_sales: {compare_to_person.sales}',
                                                 f'other_sales: {other.sales}']))
    except Exception as e:
        methods_section.add_items(
            Test('compare_to - equal', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]),
            Test('compare_to - less than', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e]),
            Test('compare_to - greater than', True, False, show_actual_expected=False,
                 data=['Test could not run due to an exception', e])
        )

    # # __str__
    string_sale_person = make_sales_person_with_sales(SALES_PERSON_ID, SALES_PERSON_NAME, sale_amount_1, sale_amount_2)

    def string_id_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        return int(emp_id)

    def string_name_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        name, total_sales = rest.split(':')
        return name

    def string_total_sales_test():
        to_string = string_sale_person.__str__()
        emp_id, rest = to_string.split('-')
        name, total_sales = rest.split(':')
        return float(total_sales.strip())

    methods_section.add_items(Test('__str__ (id)', string_id_test, SALES_PERSON_ID))
    methods_section.add_items(Test('__str__ (name)', string_name_test, SALES_PERSON_NAME))
    methods_section.add_items(Test('__str__ (total sales)', string_total_sales_test, sale_amount_1 + sale_amount_2))

    return constructor_section, instance_variables_section, methods_section


def sales_force_test():
    # Test Constructor
    constructor_section = Section('constructor')
    outcome, sales_force = run_safe(lambda: SalesForce())
    if not outcome:
        print('\nFAILED: Could not construct SalesForce, no more test will run.')
        sys.exit(1)
    outcome, _ = run_safe(lambda: SalesPerson(1, 'test'))
    if not outcome:
        print('\nFAILED: Could not construct SalesPerson, no more test will run.')
        sys.exit(1)

    constructor_section.add_items(Test('initialize constructor', True, True, show_actual_expected=False))

    # test instance variables
    instance_variable_section = Section('instance variables')
    instance_variable_section.add_items(
        Test("instance variable sales_people", lambda: type(sales_force.sales_people), list))

    # test methods
    methods_section = Section('methods')
    # add_data
    sales_data = build_sales_data(5)
    file_name = 'test_hw10_data_b02fce0e'
    write_sales_data(sales_data, file_name)

    def add_data_test(file):
        sf = SalesForce()
        sf.add_data(file)
        return sf

    outcome, result = run_safe(lambda: add_data_test(file_name))
    for index, data in enumerate(sales_data):
        if outcome:
            seller = result.sales_people[index]
            methods_section.add_items(Test(f"add_data {index} - employee_id", seller.employee_id, data[0]))
            methods_section.add_items(Test(f"add_data {index} - name", seller.name, data[1]))
            methods_section.add_items(Test(f"add_data {index} - sales", seller.sales, data[2]))
        else:
            methods_section.add_items(Test(f"add_data {index} - employee_id - unable to write sales data", True, False,
                                           show_actual_expected=False))
            methods_section.add_items(
                Test(f"add_data {index} - name - unable to write sales data", True, False, show_actual_expected=False))
            methods_section.add_items(
                Test(f"add_data {index} - sales - unable to write sales data", True, False, show_actual_expected=False))
    os.remove(file_name)

    # quota_report
    def fail_quota_report(sales_force_amount):
        for i in range(sales_force_amount):
            methods_section.add_items(
                Test(f'quota_report {i} - unable to run test - employee_id', True, False, show_actual_expected=False),
                Test(f'quota_report {i} - unable to run test - name', True, False, show_actual_expected=False),
                Test(f'quota_report {i} - unable to run test - total sales', True, False, show_actual_expected=False),
                Test(f'quota_report {i} - unable to run test - hit quota', True, False, show_actual_expected=False)
            )

    quota = random.randint(200, 700)
    sales_force_amount = 5
    quota_sales_force_data_expected = build_sales_data(sales_force_amount)
    quota_sales_force = get_full_sales_force(quota_sales_force_data_expected)
    if quota_sales_force:
        outcome, quota_report_actual = run_safe(lambda: quota_sales_force.quota_report(quota))
        if outcome:
            for i in range(sales_force_amount):
                total_sales = sum(quota_sales_force_data_expected[i][2])
                methods_section.add_items(
                    Test(f'quota_report {i} - employee_id', quota_report_actual[i][0],
                         quota_sales_force_data_expected[i][0],
                         data=print_friendly_sales_data(quota_sales_force_data_expected)),
                    Test(f'quota_report {i} - name', quota_report_actual[i][1], quota_sales_force_data_expected[i][1],
                         data=print_friendly_sales_data(quota_sales_force_data_expected)),
                    Test(f'quota_report {i} - total sales', quota_report_actual[i][2], total_sales,
                         data=print_friendly_sales_data(quota_sales_force_data_expected)),
                    Test(f'quota_report {i} - hit quota', quota_report_actual[i][3], total_sales >= quota,
                         data=print_friendly_sales_data(quota_sales_force_data_expected))
                )
            pass
        else:
            fail_quota_report(sales_force_amount)
    else:
        fail_quota_report(sales_force_amount)

    # top_seller one
    expected_top_seller = SalesPerson(701, get_random_full_name())
    expected_top_seller.enter_sale(random.randint(7000, 80000))
    top_seller_sales_force_data = build_sales_data(5)
    top_seller_sales_force = get_full_sales_force(top_seller_sales_force_data)
    if top_seller_sales_force:
        top_seller_sales_force.sales_people.append(expected_top_seller)
        methods_section.add_items(
            Test('top_seller - one', lambda: top_seller_sales_force.top_seller(), [expected_top_seller],
                 data=print_friendly_sales_data(top_seller_sales_force_data, expected_top_seller)))
    else:
        methods_section.add_items(
            Test('top_seller - one - could not create sales force', False, True, show_actual_expected=False))

    # top_seller many
    expected_top_seller_many = SalesPerson(701, get_random_full_name())
    expected_top_seller_many.enter_sale(random.randint(7000, 80000))
    top_seller_many_sales_force_data = build_sales_data(5)
    top_seller_many_sales_force = get_full_sales_force(top_seller_many_sales_force_data)
    if top_seller_many_sales_force:
        top_seller_many_sales_force.sales_people.append(expected_top_seller_many)
        top_seller_many_sales_force.sales_people.append(expected_top_seller_many)
        methods_section.add_items(
            Test('top_seller - multiple', lambda: top_seller_many_sales_force.top_seller(),
                 [expected_top_seller_many, expected_top_seller_many],
                 data=print_friendly_sales_data(top_seller_many_sales_force_data, expected_top_seller_many,
                                                expected_top_seller_many)))
    else:
        methods_section.add_items(
            Test('top_seller - multiple - could not create sales force', False, True, show_actual_expected=False))

    # individual_sales
    individual_seller_one = SalesPerson(7, get_random_full_name())
    individual_sales_sales_force_data = build_sales_data(5)
    individual_seller_sales_force = get_full_sales_force(individual_sales_sales_force_data)
    if individual_seller_sales_force:
        individual_seller_sales_force.sales_people.insert(
            random.randrange(0, len(individual_seller_sales_force.sales_people)), individual_seller_one)
        methods_section.add_items(
            Test('individual_sales - exists', lambda: individual_seller_sales_force.individual_sales(7),
                 individual_seller_one,
                 data=print_friendly_sales_data(individual_sales_sales_force_data,
                                                individual_seller_one)))
        methods_section.add_items(
            Test('individual_sales - does not exist', lambda: individual_seller_sales_force.individual_sales(8), None,
                 data=print_friendly_sales_data(individual_sales_sales_force_data, individual_seller_one)))
    else:
        methods_section.add_items(
            Test('individual_sales - exists - could not create sales force', True, False, show_actual_expected=False))

    return constructor_section, instance_variable_section, methods_section


def get_full_sales_force(data):
    try:
        sf = SalesForce()
        for d in data:
            person = SalesPerson(d[0], d[1])
            person.sales = d[2]
            sf.sales_people.append(person)
        return sf
    except:
        return None


def get_seller_data(seller: SalesPerson):
    if seller:
        return {
            'employee_id': seller.employee_id,
            'name': seller.name,
            'sales': seller.sales
        }
    return None


def get_list_seller_data(sellers: list[SalesPerson]):
    data = []
    for seller in sellers:
        data.append(get_seller_data(seller))
    return data


def get_random_name():
    name_letters = random.randint(3, 10)
    name = ''
    for i in range(name_letters):
        letter_index = random.randint(0, 25)
        letter = chr(ord('a') + letter_index)
        name += letter
    return name


def get_random_full_name():
    return get_random_name() + ' ' + get_random_name()


def print_friendly_sales_data(sales_data, *args: SalesPerson):
    data = []
    for id, name, sales in sales_data:
        data.append(f'id: {id}, name: {name}, sales: {sales}')
    for person in args:
        data.append(f'id: {person.employee_id}, name: {person.name}, sales: {person.sales}')
    return data


def build_sales_data(number_of_sales_people):
    """
    returns a list of sales people
    [
        [id, name, sales]
    ]
    """
    data = []
    for i in range(1, number_of_sales_people + 1):
        id = random.randint(i * 100 + 1, i * 100 + 100)
        name = get_random_full_name()
        sales_count = random.randint(1, 5)
        sales = []
        for j in range(sales_count):
            sales.append(round(random.uniform(100, 500), 2))
        data.append([id, name, sales])
    return data


def write_sales_data(data, file_name):
    with open(file_name, 'w') as test_data_file:
        for person in data:
            id = str(person[0])
            name = person[1]
            sales = ' '.join(map(str, person[2]))
            test_data_file.write(f'{id}, {name}, {sales}\n')
