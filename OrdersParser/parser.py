import re

from data_gateway.disk import get_sanitized_content_of_file
from . import constants
from .DossierData import DossierData


def remove_whitespaces(line):
    return line.replace(" ", "")


def get_order_dossiers(order_txt_file_path):
    """Get the order dossiers.

    Parameters:
        order_txt_file_path (str): the order txt file path.

    Return:
        tuple of (str, list of DossierData): the order number and the list of found dossiers.
    """
    order_file_content = get_sanitized_content_of_file(order_txt_file_path)

    order_number = None
    carry = None
    for line in order_file_content:
        line = remove_whitespaces(line)

        if carry is not None:
            line = carry + line
            carry = None

        order_number_matches = re.search(constants.ORDER_NUMBER_REGEX, line, re.IGNORECASE)
        if order_number_matches is not None:
            order_number_results = order_number_matches.groups()
            if len(order_number_results) != 1:
                raise Exception("Can't parse the order number.")
            order_number, = order_number_results
            order_number = order_number.replace("/", "")
            order_number = remove_whitespaces(order_number)
            break
        elif constants.ORDER_DESCRIPTION in line:
            carry = line

    if not order_number:
        raise Exception("Couldn't find the order number in file {}.".format(order_txt_file_path))

    dossiers_list = []
    for line in order_file_content:
        line = remove_whitespaces(line)
        if constants.ORDER_DESCRIPTION in line:
            continue
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

    return order_number, dossiers_list
