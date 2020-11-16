import os
from collections import defaultdict

from data_gateway import web, disk
from cetatenie_just_ro_parser import *
from pdf2txt import *
from orders_parser.parser import *
import paths
from Downloader import *


def get_all_files_in_folder(folder_path, file_type):
    """Returns all files with a file_type in the folder_path.

    Parameters:
        folder_path (str): the folder path.
        file_type (str): the file type.

    Returns:
        list of str: the list of files.
    """
    folder_items = os.listdir(folder_path)
    folder_items_paths = [str(folder_path.joinpath(i)) for i in folder_items]
    folder_files_paths = [f for f in folder_items_paths if os.path.isfile(f)]
    return [f for f in folder_files_paths if f.endswith(file_type)]


def extract_dossiers(verbose=False):
    """Extract the dossiers."""
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

    # Retrieve dossiers from TXTs and organize them by year
    if verbose:
        print("Step 5. Retrieve dossiers from TXTs")
    dossiers_by_year = defaultdict(dict)
    txt_file_paths = get_all_files_in_folder(paths.get_orders_storage_folder_path(), '.txt')
    for file_path in txt_file_paths:
        try:
            order_number, order_dossiers = get_order_dossiers(file_path, constants.DOSSIER_REGEX)
        except:
            order_number, order_dossiers = get_order_dossiers(file_path, constants.DOSSIER_REGEX_NO_PARENTHESES)

        for d in order_dossiers:
            if d.number in dossiers_by_year[d.year]:
                if verbose:
                    print("This dossier already exists: {} / {}.".format(d.number, d.year), end=' ')
                if dossiers_by_year[d.year][d.number] == order_number:
                    if verbose:
                        print("But it has the same order value.")
                else:
                    if verbose:
                        print("Currently set for order {}. New value: {}".format(dossiers_by_year[d.year][d.number], order_number))
                    orders_per_dossier = [dossiers_by_year[d.year][d.number], order_number]
                    dossiers_by_year[d.year][d.number] = orders_per_dossier
            else:
                dossiers_by_year[d.year][d.number] = order_number

    # Save the dossiers
    if verbose:
        print("Step 6. Save the dossiers.")
    for year in dossiers_by_year.keys():
        dossiers_file_path = paths.get_dossiers_collection_file_path_for_year(year)
        disk.write_dictionary_to_file(dossiers_by_year[year], dossiers_file_path)

    # Done
    if verbose:
        print("Done!")


def search(dossier_number, year):
    """Lookup a dossier in the extracted dossiers by its number and year.

    Parameters:
        dossier_number: (str): the dossier number.
        year (int): the dossier year.
    """
    # Retrieve the dossiers for the year
    year_dossiers_txt_file_path = paths.get_dossiers_collection_file_path_for_year(year)
    dossiers = disk.get_dictionary_from_file(year_dossiers_txt_file_path)
    try:
        print(dossiers[dossier_number])
    except:
        print("Not found!")


if __name__ == '__main__':
    paths.setup()

    extract_dossiers(verbose=True)

    lookups = [
        (12345, 2010),
        (12346, 2019),
    ]

    for l in lookups:
        search(str(l[0]), l[1])

    paths.cleanup()
