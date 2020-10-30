import os
import shutil

import pdf2image
from PIL import Image as PILImage
import pytesseract

import paths
from . import constants


def convert_pdf_to_txt(pdf_input_file_path, text_output_file_path, verbose=False):
    """Convert a pdf file to a txt file.

    Parameters:
        pdf_input_file_path (str): the path for the pdf file.
        text_output_file_path (str): the path for the text file.
        verbose (bool): flag to indicate the verbosity.
    """
    if os.path.exists(text_output_file_path):
        if verbose:
            print("The TXT file already exists.")
        return

    # Create a temporary folder to store temporary files
    temporary_folder_path = paths.get_storage_folder_path().joinpath(constants.TEMPORARY_FOLDER_NAME)
    if not os.path.exists(temporary_folder_path):
        os.mkdir(temporary_folder_path)

    # Convert the PDF file to images
    if verbose:
        print("Converting {} to a text file.".format(pdf_input_file_path))
    images_paths = convert_pdf_to_images(pdf_input_file_path, temporary_folder_path)

    # Convert images to TXT
    convert_images_to_txt(images_paths, text_output_file_path)

    # Remove the temporary folder path
    if verbose:
        print("Converting cleaning up.")
    shutil.rmtree(temporary_folder_path)


def convert_pdf_to_images(pdf_input_file_path, images_output_folder):
    """Convert a pdf file into a series of images.

    Parameters:
        pdf_input_file_path (str): the path for the pdf file.
        images_output_folder (str): the folder path for the images

    Return:
        list of str: the list of the resulting images' paths
    """
    # Convert PDF to images
    pdf_images = pdf2image.convert_from_path(pdf_input_file_path, constants.IMAGE_QUALITY_DPI)

    # Store the images
    pdf_images_paths = []
    for index, page in enumerate(pdf_images):
        image_file_name = constants.IMAGE_FILE_NAME_FORMAT.format(index + 1)
        image_file_path = os.path.join(images_output_folder, image_file_name)
        page.save(image_file_path, constants.IMAGE_FILE_FORMAT)
        pdf_images_paths.append(image_file_path)

    # Return the images' paths
    return pdf_images_paths


def convert_images_to_txt(image_files_paths, text_output_file_path):
    """Convert images to a text file.

    Parameters:
        image_files_paths (list of str): the list of images paths.
        text_output_file_path (str): the path for the output text file.
    """
    text_file = open(text_output_file_path, 'w')
    for ifp in image_files_paths:
        image = PILImage.open(ifp)
        image_text = str(pytesseract.image_to_string(image, config=constants.TESSERACT_CONFIGS))
        text_file.write(image_text)
    text_file.close()
