class PublishingData:
    """Stores the parsed publishing data.

    Attributes:
        publishing_date (str): the publishing date string.
        orders (list of Orders): a list of orders.
    """

    def __init__(self, publishing_date):
        """Initialize a PublishingData object.

        Parameters:
            publishing_date (str): the publishing date string.
        """
        self.publishing_date = publishing_date
        self.orders = []

    def add_order(self, order):
        """Add an order to the publishing.

        Parameters:
            order (Order): the order.
        """
        order.publishing = self
        self.orders.append(order)
