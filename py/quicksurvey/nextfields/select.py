"""
Functions to make the selection of the next field to be observed.
Most of this depends on dates, observatory position and moon.
"""

def all_available_files(directory="./", condition="*"):
    """
    Returns the list of all files in a directory matching some string 
    condition.
    
    Args:
        directory (stri): Parameter. Path to the directory to search. 
            Defaults to "./"
        condition (str): Parameter. Condition to search in the directory.
            Defaults to "*"

    Returns:
        filename_list: list of filenames in 'directory' matching 'condition'
    """
    import glob

    filename_list = glob.glob(directory + '/' + condition)

    return filename_list

    
