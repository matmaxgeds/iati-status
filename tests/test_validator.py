import pytest
from web_test_base import *

class TestIATIValidator(WebTestBase):
    requests_to_load = {
        'IATI Validator': {
            'url': 'http://validator.iatistandard.org/'
        }
    }

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://iatistandard.org/" in result

    def test_contains_form(self, loaded_request):
        """
        Test that the validator contains a form on each of three tabs.
        """
        assert len(utility.locate_xpath_result(loaded_request, '//*[@id="status"]/div/form')) == 1
        assert len(utility.locate_xpath_result(loaded_request, '//*[@id="fileTab"]/div/form')) == 1
        assert len(utility.locate_xpath_result(loaded_request, '//*[@id="extra"]/div/form')) == 1
