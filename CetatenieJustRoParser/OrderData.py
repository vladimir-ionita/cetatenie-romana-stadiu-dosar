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
        sanitized_name = name.replace(" ", "")
        if len(sanitized_name) == 0:
            sanitized_name = link.split('/')[-1]
        self.name = sanitized_name

        if len(link) == 0:
            raise Exception("There is no order for the link.")
        self.link = link

        self.publishing = None
