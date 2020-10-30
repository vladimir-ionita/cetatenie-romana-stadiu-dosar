from web import *
from CetatenieJustRoParser import *
from PublishingsDownloader import *


def run():
    # Retrieve the html content
    html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_URL)

    # Retrieve publishings
    publishings = retrieve_publishings(html_content)

    # Download publishings
    download_publishings(publishings, verbose=True)


if __name__ == '__main__':
    run()
