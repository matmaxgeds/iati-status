from lxml import etree
import pytest
import requests

class WebTestBase:
    urls_to_get = []
    initial_num_urls_to_test = len(urls_to_get)
    """
    Will hold request objects from loading each of the URLS in self.urls
    Keys are the urls themselves
    Values are the request objects
    """
    loaded_requests = dict()

    def _locate_xpath_result(self, request, xpath):
        """
        Takes a Request object and an xpath.
        Locates all instances of the specified xpath content within the html
        associated with the request.
        Returns a list of all the content matching the xpath
        """
        parser = etree.HTMLParser()
        tree = etree.fromstring(request.text, parser)
        return tree.xpath(xpath)

    def _get_links_from_page(self, request):
        """
        Locates the location of all <a href="...">...</a> tags on the page associated
        with the provided request.
        Returns a list of strings containing the linked URLs
            ie. the contents of the `href` attribute
        """
        return  self._locate_xpath_result(request, "//a[@href]/@href")

    @classmethod
    def setup_class(cls):
        """
        Initialise the class
        Loads data from each of the required URLs
        """
        for url in cls.urls_to_get:
            result = requests.get(url)
            cls.loaded_requests[url] = result
        cls.num_urls = len(cls.urls_to_get)

    def pytest_generate_tests(cls, metafunc):
        """
        Dynamically parametrizes fixtures after initialisation
        """
        if 'urls_to_get' in metafunc.fixturenames:
            metafunc.parametrize("urls_to_get", cls.urls_to_get)

    @pytest.fixture
    def loaded_request(cls, urls_to_get):
        """
        Converts the parametrized URL into loaded Request object that has
        already been initialised.
        """
        return cls.loaded_requests[urls_to_get]

    def test_200_response(self, loaded_request):
        """
        Tests that each loaded request has a status code of 200.
        """
        assert loaded_request.status_code == 200

    def test_num_urls(self):
        """
        Ensure that urls from a child class are being correctly detected
        """
        assert len(self.urls_to_get) > self.initial_num_urls_to_test
