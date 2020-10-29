from pathlib import Path
from . import constants


def get_repository_folder_path():
    """Return the repository folder path.

    Return:
        Path: the repository folder path
    """
    return Path.home().joinpath(constants.REPOSITORY_PATH)


def get_publishing_folder_name(publishing):
    """Return the publishing folder name.

    Parameters:
        publishing (PublishingData): a publishing.

    Return:
        str: the publishing folder name.
    """
    return publishing.publishing_date


def get_order_file_name(order):
    """Return the order file name.

    Parameters:
        order (OrderData): an order.

    Return:
        str: the order file name.
    """
    return "Ordinul {}.pdf".format(order.name)
