import pytest

from web_test_base import *

"""
A class to test new features without running all of the tests.

Usage:
    py.test tests/test_test.py -rsx
"""
class TestTest(WebTestBase):
    urls_to_get = [
        "http://iatistandard.org/"
        , "http://iatistandard.org/202/namespaces-extensions/"
    ]
    urls_to_post = {
        "http://validator.iatistandard.org/index.php": {'paste': 'jim bob 17'}
    }

    @pytest.mark.parametrize("target_url", ["http://iatistandard.org/"])
    def test_locate_text(self, target_url):
        """
        Tests that each page contains lthe specified text at the required location.
        """
        req = self.loaded_request_from_url(target_url)
        text_to_find = "technical publishing framework"
        xpath_to_locate = '//*[@id="home-strapline"]/h1'

        result = utility.get_text_from_xpath(req, xpath_to_locate)

        assert utility.substring_in_list(text_to_find, result)

    @pytest.mark.parametrize("target_url", ["http://validator.iatistandard.org/index.php"])
    def test_invalid_xml(self, target_url):
        """
        Tests that each page contains lthe specified text at the required location.
        """
        req = self.loaded_request_from_url(target_url)
        text_to_find = "This is not a well-formed xml file"
        xpath_to_locate = '//*[@id="status"]/div[2]'

        result = utility.get_text_from_xpath(req, xpath_to_locate)

        assert utility.substring_in_list(text_to_find, result)
