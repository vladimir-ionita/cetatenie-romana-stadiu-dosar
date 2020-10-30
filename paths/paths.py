from pathlib import Path
from . import constants


def get_storage_folder_path():
    """Return the repository folder path.

    Return:
        Path: the repository folder path.
    """
    return Path.home().joinpath(constants.FILES_STORAGE_PATH)


def get_publishings_storage_folder_path():
    """Return the publishings repository folder path.

    Return:
        Path: the publishings repository folder path.
    """
    return Path.home().joinpath(constants.PUBLISHINGS_STORAGE_PATH)


def get_publishing_folder_path(publishing):
    """Return the publishing folder path.

    Parameters:
        publishing (PublishingData): a publishing.

    Return:
        Path: the publishing folder path.
    """
    publishing_folder_name = publishing.name
    return get_publishings_storage_folder_path().joinpath(publishing_folder_name)


def get_order_pdf_file_path(order):
    """Return the order PDF file path.

    Parameters:
        order (OrderData): the order.

    Return:
        Path: the order PDF file path.
    """
    order_file_name = "Ordinul {}.pdf".format(order.name)
    return get_publishing_folder_path(order.publishing).joinpath(order_file_name)


def get_order_txt_file_path(order):
    """Return the order TXT file path.

    Parameters:
        order (OrderData): the order.

    Return:
        Path: the order TXT file path.
    """
    order_file_name = "Ordinul {}.txt".format(order.name)
    return get_publishing_folder_path(order.publishing).joinpath(order_file_name)
