class TestCase:

    def __init__(self, roads):
        '''
        roads: array of roads surveyed
        total_cars: the final car count
        avg_cars: average number of cars per road
        '''
        self.roads = roads
        self.expected_total_cars = 0
        for road in self.roads:
            self.expected_total_cars += sum(road.cars_per_day)
        self.expected_avg_cars = round(self.expected_total_cars / len(roads), 2)
        self.actual_total_cars = 0
        self.actual_avg_cars = 0
        self.total_tests = len(roads) + 2

    def parse_value(self, sentence):
        return sentence.split(':')[1].strip()

    def get_user_input(self):
        inp = [len(self.roads)]
        for road in self.roads:
            inp += road.get_user_input()
        return list(map(str, inp))

    def set_actual_values(self, user_output):
        self.actual_avg_cars = user_output.pop(len(user_output) - 1)
        self.actual_total_cars = user_output.pop(len(user_output) - 1)
        for index, road_avg in enumerate(user_output):
            self.roads[index].actual_output = road_avg


class Road:

    def __init__(self, id, cars_per_day):
        self.id = id
        self.cars_per_day = cars_per_day  # array of ints
        self.days = len(self.cars_per_day)
        self.avg_cars_per_day = round(sum(self.cars_per_day) / self.days, 2)
        self.expected_output = self.avg_cars_per_day
        self.actual_output = None

    def total_cars(self):
        return sum(self.cars_per_day)

    def get_user_input(self):
        """
        gets the user input for this road
        """
        return [self.days] + self.cars_per_day
