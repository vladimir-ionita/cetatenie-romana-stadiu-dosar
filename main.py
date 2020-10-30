from collections import defaultdict

from data_gateway import web, disk
from CetatenieJustRoParser import *
from PublishingsDownloader import *
from pdf2txt import *
from OrdersParser.parser import *
import paths


def run(verbose=False):
    # Retrieve the html content
    if verbose:
        print("Step 1. Retrieve the html content.")
    html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_WEB_PAGE_URL)

    # Retrieve publishings data
    if verbose:
        print("Step 2. Retrieve the publishings.")
    publishings = retrieve_publishings(html_content)
    if verbose:
        print("\t{} publishings found".format(len(publishings)))

    # Download publishings
    if verbose:
        print("Step 3. Download the publishings.")
    download_publishings(publishings, verbose)

    # Convert the publishings' orders from PDFs to TXTs
    if verbose:
        print("Step 4. Convert the publishings.")
    for p in publishings:
        convert_publishing_orders_from_pdf_to_txt(p, verbose)

    # Parse publishings
    if verbose:
        print("Step 5. Retrieve the dossiers.")
    dossiers = get_publishings_list_dossiers(publishings, verbose)
    if verbose:
        print("\t{} dossiers found.".format(len(dossiers)))

    # Save the dossiers
    if verbose:
        print("Step 6. Save the dossiers.")
    dossiers_years = defaultdict(list)
    for d in dossiers:
        dossiers_years[d.year].append(d.number)

    for k in dossiers_years.keys():
        dossiers_file_path = paths.get_dossiers_collection_file_path_for_year(k)
        disk.write_items_list_to_file(dossiers_years[k], dossiers_file_path)

    if verbose:
        print("Done!")


if __name__ == '__main__':
    paths.setup()
    run(verbose=True)
    paths.cleanup()
