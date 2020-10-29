from bs4 import BeautifulSoup

from CetatenieJustRoParser import constants


def extract_publishings_list_from_html(html):
    """Find and return all the publishing from the html content.
    This method finds all list items tags that contain a specific text.

    Parameters:
        html (str): the html content
    Returns:
        list of str: the list of found items
    """
    bs = BeautifulSoup(html, 'lxml')
    return bs.find_all(
        lambda tag: tag.name == constants.HTML_TAG_LIST_ITEM and constants.PUBLISHING_ITEM_TEXT in tag.text
    )
