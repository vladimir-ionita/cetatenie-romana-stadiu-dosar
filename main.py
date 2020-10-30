from data_gateway import web
from CetatenieJustRoParser import *
from PublishingsDownloader import *
from pdf2txt import *


def run():
    # Retrieve the html content
    html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_WEB_PAGE_URL)

    # Retrieve publishings data
    publishings = retrieve_publishings(html_content)

    # Download publishings
    download_publishings(publishings)

    # Convert the publishings' orders from PDFs to TXTs
    for p in publishings:
        convert_publishing_orders_from_pdf_to_txt(p)


if __name__ == '__main__':
    run()
