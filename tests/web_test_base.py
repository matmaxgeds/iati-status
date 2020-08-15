import pytest
import requests

from utility import utility


class WebTestBase:
    """
    This is a base class for all web tests.
    """

    requests_to_load = dict()
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
        timeout = 30

        for req_name, req in cls.requests_to_load.items():
            method = req.get('method', 'GET')
            kwargs = {
                'timeout': timeout,
            }
            if method == 'POST':
                kwargs['data'] = req['data']
            cls.loaded_requests[req_name] = requests.request(
                method, req['url'], **kwargs)

    def pytest_generate_tests(cls, metafunc):
        """
        Dynamically parametrizes fixtures after initialisation
        """
        if 'request_to_load' in metafunc.fixturenames:
            metafunc.parametrize("request_to_load", cls.requests_to_load.keys())

    @pytest.fixture
    def loaded_request(cls, request_to_load):
        """
        Converts the parametrized URL into loaded Request object that has
        already been initialised.
        """
        return cls.loaded_requests[request_to_load]

    def test_200_response(self, loaded_request):
        """
        Confirm each request has a 200 (success) status code.
        """
        assert loaded_request.status_code == 200

    def test_non_tiny_response(self, request_to_load):
        """
        Confirm each request has response content that is not tiny.
        """
        min_response_size = self.requests_to_load[request_to_load].get('min_response_size', 4000)
        response = self.loaded_request_from_test_name(request_to_load)

        assert len(response.content) >= min_response_size
