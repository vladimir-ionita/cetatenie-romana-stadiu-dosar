from collections import defaultdict

from data_gateway import web, disk
from CetatenieJustRoParser import *
from PublishingsDownloader import *
from pdf2txt import *
from OrdersParser.parser import *
import paths
from Downloader import *


def run_publishings(verbose=False):
    # Retrieve the html content
    if verbose:
        print("Step 1. Retrieve the html content.")
    html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_WEB_PAGE_URL)

    # Retrieve publishings data
    if verbose:
        print("Step 2. Retrieve the publishings.")
    publishings = retrieve_publishings(html_content)
    if verbose:
        print("\t{} publishings found.".format(len(publishings)))
        orders_amount = sum([len(p.orders) for p in publishings])
        print("\t{} orders found.".format(orders_amount))

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


def get_all_pdf_files_in_folder(folder_path):
    folder_items = os.listdir(folder_path)
    folder_items_paths = [str(folder_path.joinpath(i)) for i in folder_items]
    folder_files_paths = [f for f in folder_items_paths if os.path.isfile(f)]
    return [f for f in folder_files_paths if f.endswith('.pdf')]


def run_pdf_files(verbose=False):
    # Retrieve the html content
    if verbose:
        print("Step 1. Retrieve the html content.")
    # html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_WEB_PAGE_URL)

    file = open('resources/content.html')
    html_content = file.read()
    file.close()

    # Retrieve PDF links
    pdf_links = extract_pdf_links_from_html(html_content)

    # Download PDF files
    download_files(pdf_links, verbose)


if __name__ == '__main__':
    paths.setup()
    run_pdf_files(verbose=True)
    paths.cleanup()
