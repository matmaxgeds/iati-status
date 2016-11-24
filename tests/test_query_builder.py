import pytest
from web_test_base import *

class TestQueryBuilder(WebTestBase):
    urls_to_get = [
        "http://datastore.iatistandard.org/query/"
    ]

    def test_locate_links(self, loaded_request):
        """
        Tests that a page contains links to the defined URLs.
        """
        result = self._get_links_from_page(loaded_request)

        assert "http://datastore.iatistandard.org/" in result
