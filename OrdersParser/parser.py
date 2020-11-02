import re
import paths

from data_gateway.disk import get_sanitized_content_of_file
from . import constants
from .DossierData import DossierData


def get_publishings_list_dossiers(publishings_list, verbose=False):
    """Get the publishing list dossiers.

    Parameters:
        publishings_list (list of PublishingData): the list of publishings.
        verbose (bool): flag to indicate the verbosity.

    Return:
        list of DossierData: the found dossiers.
    """
    dossiers = []
    for publishing in publishings_list:
        publishing_dossiers = get_publishing_dossiers(publishing)
        if verbose:
            print("The publishing {} has {} dossiers".format(publishing.name, len(publishing_dossiers)))
        dossiers.extend(publishing_dossiers)
    return dossiers


def get_publishing_dossiers(publishing, verbose=False):
    """Get the publishing dossiers.

    Parameters:
        publishing (PublishingData): the publishing.
        verbose (bool): flag to indicate the verbosity.

    Return:
        list of DossierData: the found dossiers.
    """
    publishing_dossiers = []
    for order in publishing.orders:
        order_dossiers = get_order_dossiers(paths.get_order_txt_file_path(order))
        if verbose:
            print("The order {} has {} dossiers.".format(order.name, len(order_dossiers)))
        publishing_dossiers.extend(order_dossiers)
    return publishing_dossiers


def get_order_dossiers(order_txt_file_path):
    """Get the order dossiers.

    Parameters:
        order_txt_file_path (str): the order txt file path.

    Return:
        list of DossierData: the found dossiers.
    """
    order_file_content = get_sanitized_content_of_file(order_txt_file_path)

    dossiers_list = []
    for line in order_file_content:
        line = line.replace(" ", "")
        dossier_matches = re.search(constants.DOSSIER_REGEX, line)
        if dossier_matches is not None:
            dossier_results = dossier_matches.groups()
            if len(dossier_results) != 2:
                raise Exception("Can't parse the dossier: {}".format(line))

            dossier_number, dossier_year = dossier_results
            dossier = DossierData(dossier_number, dossier_year)
            dossiers_list.append(dossier)
    if len(dossiers_list) == 0:
        raise Exception("Couldn't find any dossiers in file {}.".format(order_txt_file_path))
