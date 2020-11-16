import os
import multiprocessing
import uuid

import pdf2image
from PIL import Image as PILImage
import pytesseract

import paths
from . import constants


def convert_pdf_files_to_txt(pdf_file_paths, verbose=False):
    """Convert a list of pdf files to txt files.

    Parameters:
        pdf_file_paths (list of str): the list of pdf file paths.
        verbose (bool): the flag to indicate the verbosity.

    """
    # Prepare the worker queue
    number_of_processes = multiprocessing.cpu_count()
    queue = multiprocessing.Queue(maxsize=number_of_processes * 2)

    # Prepare the io lock
    io_lock = None
    if verbose:
        io_lock = multiprocessing.Lock()

    # Start the pool
    pool = multiprocessing.Pool(number_of_processes, initializer=convert_pdf_files_to_txt_worker, initargs=(
        queue,
        io_lock,
        verbose
    ))

    # Fill the queue with data
    for file_path in pdf_file_paths:
        queue.put((
            file_path,
        ))

    # Stop the workers by sending the stop signal
    for _ in range(number_of_processes):
        queue.put(None)
    pool.close()
    pool.join()


def convert_pdf_files_to_txt_worker(pdf_file_paths_queue, io_lock=None, verbose=False):
    """Convert files from the file paths queue.

    Parameters:
        pdf_file_paths_queue (multiprocessing.Queue): the input queue.
        io_lock: (multiprocessing.Lock): a lock for input and output.
        verbose (bool): the flag to indicate the verbosity.
    """
    while True:
        # Get data from the queue
        try:
            queue_data = pdf_file_paths_queue.get()
        except ConnectionRefusedError:
            if verbose:
                with io_lock:
                    print("\tQueue connection refused. Retry!")
            continue

        # Stop when the queue has a None element (the break signal)
        if queue_data is None:
            break

        # Unwrap queue data
        pdf_file_path = queue_data[0]

        # Get txt file path
        txt_file_path = paths.get_order_txt_file_path_from_pdf_file_path(pdf_file_path)

        # Convert the pdf file otherwise
        convert_pdf_to_txt(pdf_file_path, txt_file_path, verbose)


def convert_pdf_to_txt(pdf_input_file_path, text_output_file_path, verbose=False):
    """Convert a pdf file to a txt file.

    Parameters:
        pdf_input_file_path (str): the path for the pdf file.
        text_output_file_path (str): the path for the text file.
        verbose (bool): flag to indicate the verbosity.
    """
    if os.path.exists(text_output_file_path) and os.stat(text_output_file_path).st_size != 0:
        if verbose:
            print("\tThe output file already exists: {}.".format(text_output_file_path))
        return

    # Convert the PDF file to images
    temporary_folder_path = paths.get_temporary_storage_folder_path()
    if verbose:
        print("\tConverting `{}` to a text file.".format(pdf_input_file_path))
    images_file_paths = convert_pdf_to_images(pdf_input_file_path, temporary_folder_path)

    # Convert images to TXT
    convert_images_to_txt(images_file_paths, text_output_file_path)
    if verbose:
        print("\tFile converted: `{}`.".format(text_output_file_path))

    # Remove the images
    for file_path in images_file_paths:
        os.remove(file_path)


def convert_pdf_to_images(pdf_input_file_path, images_output_folder):
    """Convert a pdf file into a series of images.

    Parameters:
        pdf_input_file_path (str): the path for the pdf file.
        images_output_folder (str): the folder path for the images

    Returns:
        list of str: the list of the resulting images' paths
    """
    # Convert PDF to images
    pdf_images = pdf2image.convert_from_path(pdf_input_file_path, constants.IMAGE_QUALITY_DPI)

    # Store the images
    pdf_images_paths = []
    for page in pdf_images:
        image_file_name = constants.IMAGE_FILE_NAME_FORMAT.format(uuid.uuid4())
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
