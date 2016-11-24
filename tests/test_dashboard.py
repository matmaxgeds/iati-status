import pytest
from web_test_base import *

class TestIATIDashboard(WebTestBase):
    urls_to_get = [
        "http://dashboard.iatistandard.org/"
    ]

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = self._get_links_from_page(loaded_request)

        assert "https://github.com/IATI/IATI-Dashboard/blob/master/README.rst" in result
