from datetime import datetime
from . import constants


class PublishingData:
    """Stores data about the publishing.

    Attributes:
        name (str): the publishing name.
        orders (list of Orders): the list of orders of the publishing.
    """

    def __init__(self, publishing_date_string):
        """Initialize a PublishingData object.

        Parameters:
            publishing_date_string (str): the publishing date string.
        """
        # Change the date format to from dd.mm.yyyy to yyyy.mm.dd, for easier folder navigation
        publishing_date = datetime.strptime(publishing_date_string, constants.PUBLISHING_DATE_INPUT_FORMAT)
        self.name = publishing_date.strftime(constants.PUBLISHING_DATE_OUTPUT_FORMAT)
        self.orders = []

    def add_order(self, order):
        """Add an order to the publishing.

        Parameters:
            order (Order): the order.
        """
        order.publishing = self
        self.orders.append(order)
