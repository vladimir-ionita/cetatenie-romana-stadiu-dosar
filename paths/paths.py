import os

from pathlib import Path
from . import constants


def setup():
    """Create storage folders."""
    get_storage_folder_path().mkdir(parents=True, exist_ok=True)
    get_publishings_storage_folder_path().mkdir(parents=True, exist_ok=True)
    get_temporary_storage_folder_path().mkdir(parents=True, exist_ok=True)
    get_dossiers_storage_folder_path().mkdir(parents=True, exist_ok=True)
    get_orders_storage_folder_path().mkdir(parents=True, exist_ok=True)


def cleanup():
    """Cleanup the temporary storage."""
    for item in os.listdir(get_temporary_storage_folder_path()):
        os.remove(item)


def get_storage_folder_path():
    """Return the storage folder path.

    Return:
        Path: the storage folder path.
    """
    return Path.home().joinpath(constants.FILES_STORAGE_PATH)


def get_publishings_storage_folder_path():
    """Return the publishings storage folder path.

    Return:
        Path: the publishings storage folder path.
    """
    return Path.home().joinpath(constants.PUBLISHINGS_STORAGE_PATH)


def get_temporary_storage_folder_path():
    """Return the temporary storage folder path.

    Return:
        Path: the temporary storage folder path.
    """
    return Path.home().joinpath(constants.TEMPORARY_STORAGE_PATH)


def get_dossiers_storage_folder_path():
    """Return the dossiers storage folder path.

    Return:
        Path: the dossiers storage folder path.
    """
    return Path.home().joinpath(constants.DOSSIERS_STORAGE_PATH)


def get_orders_storage_folder_path():
    """Return the orders storage folder path.

    Returns:
        Path: the orders storage folder path.
    """
    return get_storage_folder_path().joinpath(constants.ORDERS_STORAGE_FOLDER_PATH)


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


def get_dossiers_collection_file_path_for_year(year):
    """Return the dossiers collection file path.

    Parameters:
        year (int): the dossier collection year

    Return:
        Path: the dossiers collection file path.
    """
    dossiers_collection_file_name = "Dossiers {}.txt".format(year)
    return get_dossiers_storage_folder_path().joinpath(dossiers_collection_file_name)
