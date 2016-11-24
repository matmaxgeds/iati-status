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
    text_to_find = [
        ("technical publishing framework", '//*[@id="home-strapline"]/h1')
    ]

    def test_locate_text(self, loaded_request, text_to_find):
        """
        Tests that each page contains lthe specified text at the required location.
        """
        result = self._get_text_from_xpath(loaded_request, text_to_find[1])

        assert self._substring_in_list(text_to_find[0], result)
