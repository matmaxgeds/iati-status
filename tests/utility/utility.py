from lxml import etree

import os

def locate_xpath_result(request, xpath):
    """
    Takes a Request object and an xpath.
    Locates all instances of the specified xpath content within the html
    associated with the request.
    Returns a list of all the content matching the xpath
    """
    parser = etree.HTMLParser()
    tree = etree.fromstring(request.text, parser)
    return tree.xpath(xpath)

def get_links_from_page(request):
    """
    Locates the location of all <a href="...">...</a> tags on the page
    associated with the provided request.
    Returns a list of strings containing the linked URLs
        ie. the contents of the `href` attribute
    """
    return locate_xpath_result(request, "//a[@href]/@href")

def get_text_from_xpath(request, xpath):
    """
    Locates the notes within the HTML at the specific xpath.
    Returns a list of strings containing the contents of these nodes.
    """
    return locate_xpath_result(request, xpath + "/text()")

def substring_in_list(substr_to_find, list_to_search):
    """
    Returns a boolean value to indicate whether or not a given substring
    is located within the strings of a list.
    """
    return len([s for s in list_to_search if substr_to_find in s]) > 0

def get_data_folder():
    """
    Returns the location of the folder containing data files.
    """
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')
    return os.path.normpath(path)

def get_data_file(file_name):
    """
    Returns a path to a data file with the given name.
    """
    return os.path.join(get_data_folder(), file_name)

def load_file_contents(file_name):
    """
    Reads the contents of a file into a string.
    Returns a string containing the file contents.
    """
    with open(get_data_file(file_name), 'r') as myfile:
        data = myfile.read()
    return data
