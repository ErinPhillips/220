"""
Name: Erin Phillips
sales_person.py

Problem: this program encapsulates data for a sales person

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """SalesPerson class is used to hold sales person object data."""

    def __init__(self, employee_id, name):
        """ SalesPerson Class Constructor to initialize the object.

        Input Arguments: employee_id must be an int, name must be a str
        eg. SalesPerson(123, "Jane Doe")
        """
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """Returns the employee_id of this SalesPerson -> int. """
        return self.employee_id

    def get_name(self):
        """Returns the name of the this SalesPerson -> str."""
        return self.name

    def set_name(self, name):
        """ Sets the name of this SalesPerson to the specified parameter.

        Input Arguments: name must be str
        """
        self.name = name

    def enter_sale(self, sale):
        """ Adds the sale value to the list of sales for this SalesPerson.

        Input Arguments: sale must be a numeric value
        """
        self.sales += [sale]

    def total_sales(self):
        """ This method totals all sales of this SalesPerson -> float."""
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        """Returns a list of sale values for this SalesPerson -> list."""
        return self.sales

    def met_quota(self, quota):
        """ This method checks if SalesPerson object has met the specified quota
        and returns a boolean value.

        Input Arguments: quota must be a numeric value
        Returns: True if quota is met, False if quota is not met.
        """
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        """ This method compares the total sales of two SalesPerson objects; self and other.

        Input Arguments: other must be another SalesPerson object.
        Returns: 1 if self has more in total sales.
        -1 if other has more in total sales.
        0 if self and other total sales are equal.
        """
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() < other.total_sales():
            return -1
        return 0

    def __str__(self):
        """ Returns SalesPerson data "<employee_id>-<name>: <total sales>" -> str."""
        return str(self.employee_id) + "-" + str(self.name) + ": " + str(self.total_sales())
