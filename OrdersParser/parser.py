import re
import paths

from data_gateway.disk import get_sanitized_content_of_file
from . import constants
from .DossierData import DossierData


def get_order_dossiers(order):
    """Get the order dossiers.
    Parse the order file for dossiers.

    Parameters:
        order (OrderData): the order.

    Return:
        list of DossierData: the found dossiers.
    """
    order_file_path = paths.get_order_txt_file_path(order)
    order_file_content = get_sanitized_content_of_file(order_file_path)

    dossiers_list = []
    for line in order_file_content:
        dossier_matches = re.search(constants.DOSSIER_REGEX, line)
        if dossier_matches is not None:
            dossier_results = dossier_matches.groups()
            if len(dossier_results) != 2:
                raise Exception("Can't parse the dossier: {}".format(line))

            dossier_number, dossier_year = dossier_results
            dossier = DossierData(dossier_number, dossier_year)
            dossiers_list.append(dossier)
    return dossiers_list
