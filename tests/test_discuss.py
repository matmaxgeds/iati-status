import pytest
from web_test_base import *

class TestIATIDiscuss(WebTestBase):
    urls_to_get = [
        "http://discuss.iatistandard.org/"
    ]

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://iatistandard.org/" in result
