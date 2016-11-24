import pytest
from web_test_base import *

class TestAidinfolabsCSVConverter(WebTestBase):
    urls_to_get = [
        "http://tools.aidinfolabs.org/csv/direct_from_registry/"
    ]

    def test_locate_links(self, loaded_request):
        """
        Tests that a page contains links to the defined URLs.
        """
        result = self._get_links_from_page(loaded_request)

        assert "http://www.iatistandard.org" in result
