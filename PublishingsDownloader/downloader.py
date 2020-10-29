import os
from pathlib import Path

import wget
from . import paths


def download_publishings_list(publishings_list, verbose=False):
    """Download the publishing list.
    This method downloads only the missing publishings. It works like a download resume.

    Parameters:
        publishings_list (list of PublishingData): the list of publishings
        verbose (Bool): flag to indicate the verbosity
    """
    repository_folder = paths.get_repository_folder_path()
    for publishing in publishings_list:
        # If publishing was already downloaded, skip
        if is_publishing_already_downloaded(publishing, repository_folder):
            if verbose:
                print("Publishing {} already exists".format(publishing.publishing_date))
        # Download the publishing otherwise
        else:
            if verbose:
                print("Downloading publishing {}".format(publishing.publishing_date))
            download_publishing(publishing, repository_folder, verbose)


def download_publishing(publishing, folder_path, verbose=False):
    """Download a publishing to a repository folder.

    Parameters:
        publishing (PublishingData): the publishing
        folder_path (Path): the destination folder for downloads
        verbose (Bool): flag to indicate the verbosity
    """
    # Create publishing folder
    publishing_folder_name = paths.get_publishing_folder_name(publishing)
    publishing_folder_path = folder_path.joinpath(publishing_folder_name)
    publishing_folder_path.mkdir(parents=True, exist_ok=True)

    # Download orders
    for order in publishing.orders:
        download_order(order, publishing_folder_path, verbose)


def download_order(order, folder_path, verbose=False):
    """Download an order to a destination.

    Parameters:
        order (OrderData): the order
        folder_path (Path): the destination folder for downloads
        verbose (Bool): flag to indicate the verbosity
    """
    order_file_name = paths.get_order_file_name(order)
    order_file_path = folder_path.joinpath(order_file_name)

    # If file already exists, skip
    if os.path.exists(order_file_path):
        if verbose:
            print("\tOrder `{}` already exists".format(order.name))
        return

    # Download the file otherwise
    if verbose:
        print("\tDownloading order {}".format(order.name))
    wget.download(order.link, str(order_file_path))


def is_publishing_already_downloaded(publishing, repository_folder):
    """Check if a publishing is already downloaded.

    Parameters:
        publishing (PublishingData): the publishing to be checked
        repository_folder (Path): the folder path to check within

    Return:
        bool: True if the publishing was already downloaded and False otherwise
    """
    publishing_folder_name = paths.get_publishing_folder_name(publishing)
    publishing_folder_path = repository_folder.joinpath(publishing_folder_name)
    if not os.path.exists(publishing_folder_path) or not os.path.isdir(publishing_folder_path):
        return False

    for order in publishing.orders:
        order_file_name = paths.get_order_file_name(order)
        order_file_path = publishing_folder_path.joinpath(order_file_name)
        if not os.path.exists(order_file_path) or not os.path.isfile(order_file_path):
            return False
    return True
