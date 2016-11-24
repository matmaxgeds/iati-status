import pytest
from web_test_base import *

class TestAidTransparency(WebTestBase):
    urls_to_get = [
        "http://aidtransparency.net/"
        , "http://www.aidtransparency.net/"
        , "http://www.aidtransparency.net/annualreport2015/"
    ]

    def test_locate_links(self, loaded_request):
        """
        Tests that each page contains links to the defined URLs.
        """
        result = self._get_links_from_page(loaded_request)

        assert ("http://iatistandard.org/" in result) or ("http://dashboard.iatistandard.org/" in result)
        assert "http://www.aidtransparency.net" in result
