import pytest
import requests

from utility import utility

class WebTestBase:
    urls_to_get = []
    urls_to_post = dict()
    initial_num_urls_to_test = len(urls_to_get) + len(urls_to_post.keys())
    """
    Will hold request objects from loading each of the URLS in self.urls
    Keys are the urls themselves
    Values are the request objects
    """
    loaded_requests = dict()

    def loaded_request_from_url(self, url):
        """
        Returns the loaded request for a given URL.
        """
        return self.loaded_requests[url]

    @classmethod
    def setup_class(cls):
        """
        Initialise the class
        Loads data from each of the required URLs
        """
        for url in cls.urls_to_get:
            result = requests.get(url)
            cls.loaded_requests[url] = result
        for url in cls.urls_to_post.keys():
            result = requests.post(url, data=cls.urls_to_post[url])
            # TODO: Deal with the same URL being requested in multiple ways
            cls.loaded_requests[url] = result
        cls.num_urls = len(cls.urls_to_get) + len(cls.urls_to_post)

    def pytest_generate_tests(cls, metafunc):
        """
        Dynamically parametrizes fixtures after initialisation
        """
        if 'urls_to_get' in metafunc.fixturenames:
            metafunc.parametrize("urls_to_get", cls.urls_to_get)
        if 'text_to_find' in metafunc.fixturenames:
            metafunc.parametrize("text_to_find", cls.text_to_find)

    # TODO: Handle POST requests
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
