class DossierData:
    """Stores data about the dossier.

    Attributes:
        number (str): the dossier number
        year (int): the dossier application year
    """

    def __init__(self, number, year):
        """Initialize a DossierData object.

        Parameters:
            number (str): the dossier number
            year (str): the dossier application year
        """
        self.number = number
        self.year = int(year)
