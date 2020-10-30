from pathlib import Path
from . import constants


def get_repository_path():
    """Return the repository folder path.

    Return:
        Path: the repository folder path.
    """
    return Path.home().joinpath(constants.REPOSITORY_PATH)


def get_publishings_repository_path():
    """Return the publishings repository folder path.

    Return:
        Path: the publishings repository folder path.
    """
    return Path.home().joinpath(constants.PUBLISHINGS_REPOSITORY_PATH)


def get_publishing_folder_path(publishing):
    """Return the publishing folder path.

    Parameters:
        publishing (PublishingData): a publishing.

    Return:
        Path: the publishing folder path.
    """
    publishing_folder_name = publishing.publishing_date
    return get_publishings_repository_path().joinpath(publishing_folder_name)


def get_order_pdf_file_name(order):
    """Return the order PDF file name.

    Parameters:
        order (OrderData): an order.

    Return:
        str: the order PDF file name.
    """
    return "Ordinul {}.pdf".format(order.name)


def get_order_txt_file_name(order):
    """Return the order file name.

    Parameters:
        order (OrderData): an order.

    Return:
        str: the order file name.
    """
    return "Ordinul {}.txt".format(order.name)
