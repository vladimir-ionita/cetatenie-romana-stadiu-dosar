class PublishingData:
    """Stores data about the publishing.

    Attributes:
        name (str): the publishing name.
        orders (list of Orders): the list of orders of the publishing.
    """

    def __init__(self, publishing_date):
        """Initialize a PublishingData object.

        Parameters:
            publishing_date (str): the publishing date string.
        """
        self.name = publishing_date
        self.orders = []

    def add_order(self, order):
        """Add an order to the publishing.

        Parameters:
            order (Order): the order.
        """
        order.publishing = self
        self.orders.append(order)
