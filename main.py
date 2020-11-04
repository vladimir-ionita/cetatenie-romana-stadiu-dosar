import os

from data_gateway import web, disk
from CetatenieJustRoParser import *
from pdf2txt import *
from OrdersParser.parser import *
import paths
from Downloader import *


def get_all_files_in_folder(folder_path, file_type):
    folder_items = os.listdir(folder_path)
    folder_items_paths = [str(folder_path.joinpath(i)) for i in folder_items]
    folder_files_paths = [f for f in folder_items_paths if os.path.isfile(f)]
    return [f for f in folder_files_paths if f.endswith(file_type)]


def run_pdf_files(verbose=False):
    # Retrieve the html content
    if verbose:
        print("Step 1. Retrieve the html content.")
    html_content = web.get_html_content(CETATENIE_JUST_RO_ORDERS_WEB_PAGE_URL)

    # Retrieve PDF links
    if verbose:
        print("Step 2. Retrieve the PDF links.")
    pdf_links = extract_pdf_links_from_html(html_content)

    # Download PDF files
    if verbose:
        print("Step 3. Download the PDF files.")
    download_files(pdf_links, verbose)

    # Retrieve all pdf files from the folder
    pdf_file_paths = get_all_files_in_folder(paths.get_orders_storage_folder_path(), '.pdf')

    # Convert the publishings' orders from PDFs to TXTs
    if verbose:
        print("Step 4. Convert the publishings.")
    convert_pdf_files_to_txt(pdf_file_paths, verbose)


if __name__ == '__main__':
    paths.setup()
    run_pdf_files(verbose=True)
    paths.cleanup()
