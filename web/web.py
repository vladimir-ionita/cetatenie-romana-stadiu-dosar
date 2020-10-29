import requests


def get_html_content(url):
    """Get a web page html content.

    Parameters:
        url (str): the web page url
    Returns:
        str: the web page content
    """
    return requests.get(url).text
