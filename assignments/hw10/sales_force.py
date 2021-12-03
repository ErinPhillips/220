"""
Name: Erin Phillips
sales_force.py

Problem: this program defines a SalesForce class

Certificate of Authenticity
I certify that this assignment is entirely my own work.
"""
from hw10.sales_person import SalesPerson


class SalesForce:
    """SalesForce class is used to hold sales force object data."""

    def __init__(self):
        """SalesForce Class Constructor to initialize the object.

        eg. SalesForce()
        """
        self.sales_people = []

    def add_data(self, file_name):
        """This method imports information for sales people from the specified file.

        Imported data is added to the sales_people list as SalesPerson objects.
        """
        with open(file_name, "r") as file:
            for line in file:
                data = line.replace(",", "").split()
                seller = SalesPerson(float(data[0]), data[1] + " " + data[2])
                sales = data[3:]
                for sale in sales:
                    seller.enter_sale(float(sale))
                self.sales_people += [seller]

    def quota_report(self, quota):
        """This method returns a list of SalesPerson object data within a SaleForce object.

        Each element is a list containing a SalesPerson object employee id, name,
        total sales, and a boolean value of whether or not they hit the specified quota.
        True if quota is met, False if quota is not met.

        Input Arguments: quota must be a numeric value.

        Returns: [list[list[int, str, float, bool]]]
        """
        report = []
        for seller in self.sales_people:
            report.append([seller.get_id(), seller.get_name(),
                           seller.total_sales(), seller.met_quota(quota)])
        return report

    def top_seller(self):
        """Returns a list of SalesPerson(s) objects with the highest sales amount."""
        values = []
        for seller in self.sales_people:
            values.append(seller.total_sales())

        top_value = max(values)
        top_seller = []
        for seller in self.sales_people:
            if seller.total_sales() == top_value:
                top_seller.append(seller)
        return top_seller

    def individual_sales(self, employee_id):
        """This method searches for a SalesPerson object with the specified employee ID.

        Input Arguments: employee_id must be int

        Returns: string of SalesPerson object data if ID exists. None if ID does not exist.
        """
        for seller in self.sales_people:
            if seller.get_id() == employee_id:
                return seller
        return None
