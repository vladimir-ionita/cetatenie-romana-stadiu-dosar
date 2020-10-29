class OrderData:
    """Stores the parsed order data.

    Attributes:
        name (str): order name.
        link (str): order link.
    """

    def __init__(self, name, link):
        """Initialize an OrderData object.

        Parameters:
            name (str): order name.
            link (str): order link.
        """
        self.name = name
        self.link = link
