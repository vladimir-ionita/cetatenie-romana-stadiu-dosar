import json


def write_items_list_to_file(items_list, file_path):
    """Writes the list to the file.

    Parameters:
        items_list (list of str): the list to be stored.
        file_path (str): the file path.
    """
    file = open(file_path, 'w')
    for item in items_list:
        file.write("{}\n".format(item))
    file.close()


def write_dictionary_to_file(dictionary, file_path):
    """Write the dictionary to a file.

    Parameters:
        dictionary (dict): the dictionary.
        file_path (str): the file path.
    """
    json_data = json.dumps(dictionary)
    file = open(file_path, 'w')
    file.write(json_data)
    file.close()
