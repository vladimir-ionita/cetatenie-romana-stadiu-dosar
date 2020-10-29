from bs4 import BeautifulSoup

from CetatenieJustRoParser import constants
from CetatenieJustRoParser.OrderData import OrderData
from CetatenieJustRoParser.PublishingData import PublishingData


def get_publishings(html):
    """Retrieves all publishings.

    Parameters:
        html (str): the html content.

    Returns:
        list of PublishingData: a list of parsed PublishingData.
    """
    publishings_data_list = []

    # Retrieve the list of publishings
    publishings_item_list = extract_publishings_list_from_html(html)
    for item in publishings_item_list:
        # Retrieve the publishing date
        publishing_date_string = item.strong.get_text().lstrip().rstrip()
        # Create the publishing data object
        publishing_data = PublishingData(publishing_date_string)
        # Extract order links from the item
        publishing_order_links = extract_links_from_bs_tag(item)
        for order_link in publishing_order_links:
            # Retrieve order data
            order_name = order_link.get_text()
            order_link = constants.CETATENIE_JUST_RO_BASE_URL + order_link['href']
            # Create the order data object
            order_data = OrderData(order_name, order_link)
            # Append the order to the publishing
            publishing_data.add_order(order_data)
        # Store the publishing data
        publishings_data_list.append(publishing_data)

    return publishings_data_list


def extract_publishings_list_from_html(html):
    """Find and return all the publishing from the html content.
    This method finds all list items tags that contain a specific text.

    Parameters:
        html (str): the html content.
    Returns:
        list of str: the list of found items.
    """
    bs = BeautifulSoup(html, 'lxml')
    return bs.find_all(
        lambda tag: tag.name == constants.HTML_TAG_LIST_ITEM and constants.PUBLISHING_ITEM_TEXT in tag.text
    )


def extract_links_from_bs_tag(bs_tag):
    """Find and return all links from a beautifulsoup tag.

    Parameters:
        bs_tag (bs4.Tag): the beautifulsoup tag.

    Returns:
        list of str: the list of links.
    """
    return bs_tag.find_all(constants.HTML_TAG_LINK)
