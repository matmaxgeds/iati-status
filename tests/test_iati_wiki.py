from utility import utility
from web_test_base import WebTestBase


class TestIATIWiki(WebTestBase):
    """
    Test old wiki (wiki.archive.iatistandard.org)
    """
    requests_to_load = {
        'wiki.archive.iatistandard.org': {
            'url': 'http://wiki.archive.iatistandard.org/'
        }
    }

    def test_locate_links(self, loaded_request):
        """
        Confirm each page contains links to:

        * iatistandard.org
        * iatiregistry.org
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://www.iatistandard.org" in result
        assert "http://www.iatiregistry.org" in result
