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
