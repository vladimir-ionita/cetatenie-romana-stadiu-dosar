class OrderData:
    """Stores data about the order.

    Attributes:
        name (str): order name.
        link (str): order link.
        publishing (PublishingData): the publishing of the order.
    """

    def __init__(self, name, link):
        """Initialize an OrderData object.

        Parameters:
            name (str): order name.
            link (str): order link.
        """
        self.name = name
        self.link = link
        self.publishing = None
