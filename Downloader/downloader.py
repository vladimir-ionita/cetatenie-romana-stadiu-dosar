import os
from urllib import request
from urllib.error import HTTPError
import paths


def download_files_worker(url_queue, io_lock=None, verbose=False):
    while True:
        # Get data from the queue
        try:
            queue_data = url_queue.get()
        except ConnectionRefusedError:
            if verbose:
                with io_lock:
                    print("\t\tQueue connection refused. Retry!")
            continue

        # Stop when the queue has a None element (the break signal)
        if queue_data is None:
            break

        # Unwrap queue data
        file_url = queue_data[0]

        # Get file path
        file_path = paths.get_order_pdf_file_path_from_pdf_url(file_url)

        # If file already exists, skip
        if os.path.exists(file_path):
            if verbose:
                print("\t\tFile `{}` already exists.".format(file_path))
            continue

        # Download the file otherwise
        if verbose:
            print("\t\tDownloading file `{}`".format(file_path))
        downloaded = False
        while not downloaded:
            try:
                request.urlretrieve(file_url, file_path)
                downloaded = True
            except HTTPError:
                print("\t\tHTTP Error. File not found `{}`.".format(file_url))
                break
            except Exception as e:
                if verbose:
                    print("\t\tIssue downloading {}. Exception {}: {}".format(file_url, type(e).__name__, e))
                continue
        if downloaded:
            if verbose:
                print("\t\tFile downloaded: `{}` from `{}`".format(file_path, file_url))
