import pytest
from web_test_base import *

class TestQueryBuilder(WebTestBase):
    requests_to_load = {
        'IATI Query Builder': {
            'url': 'http://datastore.iatistandard.org/query/'
        },
        'POST Example': {
            'url': 'http://datastore.iatistandard.org/query/index.php',
            'method': 'POST',
            'data': {
                'format': 'activity',
                'grouping': 'summary',
                'sample-size': '50 rows',
                'reporting-org[]': 'XM-DAC-3-1',
                'sector[]': '12181',
                'recipient-region[]': '298',
                'submit': 'Submit'
            }
        },
        'Publisher Information': {
            'url': 'http://datastore.iatistandard.org/query/helpers/groups_cache_dc.json',
            'min_response_size': 1500000
        }
    }

    @pytest.mark.parametrize("target_request", ["IATI Query Builder", "POST Example"])
    def test_locate_links(self, target_request):
        """
        Tests that a page contains links to the defined URLs.
        """
        req = self.loaded_request_from_test_name(target_request)

        result = utility.get_links_from_page(req)

        assert "http://iatistandard.org/guidance/datastore/" in result

    @pytest.mark.parametrize("target_request", ["POST Example"])
    def test_form_submit_link(self, target_request):
        """
        Tests that a result page contains a link to the relevant search.
        """
        req = self.loaded_request_from_test_name(target_request)

        result = utility.get_links_from_page(req)

        assert "http://datastore.iatistandard.org/api/1/access/activity.csv?reporting-org=XM-DAC-3-1&sector=12181&recipient-region=298" in result
