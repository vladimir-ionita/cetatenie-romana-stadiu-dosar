from bs4 import BeautifulSoup
from CetatenieJustRoParser import constants


def extract_pdf_links_from_html(html):
    """Find and return all pdf links from the html content.

    Parameters:
        html (str): the html content.

    Return:
        set of str: the set of found pdf links.
    """
    bs = BeautifulSoup(html, 'lxml')
    html_pdf_link_elements = bs.find_all(
        lambda tag: tag.name == constants.HTML_TAG_LINK and tag['href'].endswith('.pdf')
    )
    pdf_links = [constants.CETATENIE_JUST_RO_WEBSITE_BASE_URL + item['href'] for item in html_pdf_link_elements]
    return set(pdf_links)
