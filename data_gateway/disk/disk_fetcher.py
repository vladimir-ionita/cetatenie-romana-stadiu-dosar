import json


def get_raw_content_of_file(file_path):
    """Return the raw file content.

    Parameters:
        file_path (str): the file path.

    Return:
        list of str: the raw file content
    """
    file = open(file_path)
    file_content = file.readlines()
    file.close()
    return file_content


def get_sanitized_content_of_file(file_path):
    """Return the sanitized file content.

    Parameters:
        file_path (str): the file path.

    Return:
        list of str: the sanitized file content
    """
    file_content = get_raw_content_of_file(file_path)
    sanitized_file_content = []
    for line in file_content:
        sanitized_file_content.append(line.strip())
    return sanitized_file_content


def get_dictionary_from_file(file_path):
    """Read a dictionary from a file.

    Parameters:
        file_path (str): the file path.

    Returns:
        dict: the dictionary.
    """
    file = open(file_path)
    file_content = file.read()
    file.close()
    return json.loads(file_content)
