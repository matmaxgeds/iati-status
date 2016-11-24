import pytest
from web_test_base import *

class TestIATIRegistry(WebTestBase):
    urls_to_get = [
        "http://iatiregistry.org/"
        , "http://www.iatiregistry.org/"
        , "https://iatiregistry.org/"
        , "https://www.iatiregistry.org/"
    ]

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = self._get_links_from_page(loaded_request)

        assert "http://www.aidtransparency.net/" in result
        assert "http://www.iatistandard.org/" in result
