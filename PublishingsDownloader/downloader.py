import os
import wget
import paths


def download_publishings_list(publishings_list, verbose=False):
    """Download the publishing list.
    This method downloads only the missing publishings. It works like a download resume.

    Parameters:
        publishings_list (list of PublishingData): the list of publishings.
        verbose (bool): flag to indicate the verbosity.
    """
    for publishing in publishings_list:
        # If publishing was already downloaded, skip
        if is_publishing_downloaded(publishing):
            if verbose:
                print("Publishing {} already exists".format(publishing.publishing_date))
        # Download the publishing otherwise
        else:
            if verbose:
                print("Downloading publishing {}".format(publishing.publishing_date))
            download_publishing(publishing, verbose)


def download_publishing(publishing, verbose=False):
    """Download the publishing.

    Parameters:
        publishing (PublishingData): the publishing.
        verbose (bool): flag to indicate the verbosity.
    """
    # Create publishing folder
    publishing_folder_path = paths.get_publishing_folder_path(publishing)
    publishing_folder_path.mkdir(parents=True, exist_ok=True)

    # Download orders
    for order in publishing.orders:
        download_order(order, verbose)


def download_order(order, verbose=False):
    """Download the order.

    Parameters:
        order (OrderData): the order.
        verbose (bool): flag to indicate the verbosity.
    """
    order_file_path = paths.get_order_pdf_file_path(order)

    # If file already exists, skip
    if os.path.exists(order_file_path):
        if verbose:
            print("\tOrder `{}` already exists".format(order.name))
        return

    # Download the file otherwise
    if verbose:
        print("\tDownloading order {}".format(order.name))
    wget.download(order.link, str(order_file_path))


def is_publishing_downloaded(publishing):
    """Check if the publishing is downloaded.

    Parameters:
        publishing (PublishingData): the publishing to be checked.

    Return:
        bool: True if the publishing is downloaded and False otherwise.
    """
    publishing_folder_path = paths.get_publishing_folder_path(publishing)
    if not os.path.exists(publishing_folder_path) or not os.path.isdir(publishing_folder_path):
        return False

    for order in publishing.orders:
        order_file_path = paths.get_order_pdf_file_path(order)
        if not os.path.exists(order_file_path) or not os.path.isfile(order_file_path):
            return False
    return True
