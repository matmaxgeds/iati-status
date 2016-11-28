import pytest
import requests

from utility import utility

class WebTestBase:
    requests_to_load = dict()
    initial_num_urls_to_test = len(requests_to_load)
    """
    Will hold request objects from loading each of the URLS in self.urls
    Keys are the urls themselves
    Values are the request objects
    """
    loaded_requests = dict()

    def loaded_request_from_test_name(self, test_name):
        """
        Returns the loaded request for a given URL.
        """
        return self.loaded_requests[test_name]

    @classmethod
    def setup_class(cls):
        """
        Initialise the class
        Loads data from each of the required URLs
        """
        for testname, test in cls.requests_to_load.items():
            try:
                method = test['method']
            except KeyError:
                method = 'GET'

            if method == 'GET':
                result = requests.get(test['url'])
            elif method == 'POST':
                result = requests.post(test['url'], data=test['data'])
            else:
                raise ValueError('Invalid HTTP method - ' + method)

            cls.loaded_requests[testname] = result
        cls.num_urls = len(cls.requests_to_load)

    def pytest_generate_tests(cls, metafunc):
        """
        Dynamically parametrizes fixtures after initialisation
        """
        if 'requests_to_load' in metafunc.fixturenames:
            metafunc.parametrize("requests_to_load", cls.requests_to_load.keys())
        if 'text_to_find' in metafunc.fixturenames:
            metafunc.parametrize("text_to_find", cls.text_to_find)

    @pytest.fixture
    def loaded_request(cls, requests_to_load):
        """
        Converts the parametrized URL into loaded Request object that has
        already been initialised.
        """
        return cls.loaded_requests[requests_to_load]

    def test_200_response(self, loaded_request):
        """
        Tests that each loaded request has a status code of 200.
        """
        assert loaded_request.status_code == 200

    def test_num_urls(self):
        """
        Ensure that urls from a child class are being correctly detected
        """
        assert len(self.requests_to_load) > self.initial_num_urls_to_test
