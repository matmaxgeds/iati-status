from lxml import etree

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
