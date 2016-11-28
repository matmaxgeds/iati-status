import pytest
from web_test_base import *

class TestIATIRegistry(WebTestBase):
    requests_to_load = {
        'IATI Registry Homepage - http, no www': {
            'url': 'http://iatiregistry.org/'
        },
        'IATI Registry Homepage - http, with www': {
            'url': 'http://www.iatiregistry.org/'
        },
        'IATI Registry Homepage - https, no www': {
            'url': 'https://iatiregistry.org/'
        },
        'IATI Registry Homepage - https, with www': {
            'url': 'https://www.iatiregistry.org/'
        }
    }

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://www.aidtransparency.net/" in result
        assert "http://www.iatistandard.org/" in result
