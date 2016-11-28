import pytest
from web_test_base import *

class TestIATIPreview(WebTestBase):
    requests_to_load = {
        'IATI Preview': {
            'url': 'http://preview.iatistandard.org/'
        }
    }

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://www.iatistandard.org/" in result
