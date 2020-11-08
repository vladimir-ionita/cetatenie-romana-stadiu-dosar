import os

from pathlib import Path
from . import constants


def setup():
    """Create storage folders."""
    get_storage_folder_path().mkdir(parents=True, exist_ok=True)
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
    return Path.home().joinpath(constants.ORDERS_STORAGE_FOLDER_PATH)


def get_dossiers_collection_file_path_for_year(year):
    """Return the dossiers collection file path.

    Parameters:
        year (int): the dossier collection year

    Return:
        Path: the dossiers collection file path.
    """
    dossiers_collection_file_name = "Dossiers {}.txt".format(year)
    return get_dossiers_storage_folder_path().joinpath(dossiers_collection_file_name)


def get_dossiers_collection_file_path():
    """Make the dossiers collection file path.

    Returns:
        Path: the dossiers colelction file path.
    """
    return get_dossiers_storage_folder_path().joinpath(constants.DOSSIERS_FILE_NAME)


def get_order_pdf_file_path_from_pdf_url(pdf_url):
    """Return the order pdf file path from the pdf url.

    Parameters:
        pdf_url (str): the pdf url.

    Returns:
        Path: the order pdf file path.
    """
    file_name = pdf_url.split('/')[-1]
    return get_orders_storage_folder_path().joinpath(file_name)


def get_order_txt_file_path_from_pdf_file_path(pdf_file_path):
    """Return the order txt file path from the pdf file path.

    Parameters:
        pdf_file_path (str): the pdf file path.

    Returns:
        Path: the txt file path
    """
    return pdf_file_path.replace(".pdf", ".txt")
