import pytest
from web_test_base import *

class TestAidTransparency(WebTestBase):
    requests_to_load = {
        'AidTransparency Homepage - no www': {
            'url': 'http://aidtransparency.net/'
        }
        , 'AidTransparency Homepage - with www': {
            'url': 'http://www.aidtransparency.net/'
        }
        , '2015 Annual Report': {
            'url': 'http://www.aidtransparency.net/annualreport2015/'
        }
    }

    def test_locate_links(self, loaded_request):
        """
        Tests that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert ("http://iatistandard.org/" in result) or ("http://dashboard.iatistandard.org/" in result)
        assert "http://www.aidtransparency.net" in result

    @pytest.mark.parametrize("target_request", ["AidTransparency Homepage - no www", "AidTransparency Homepage - with www"])
    def test_homepage_news_items(self, target_request):
        """
        Tests that he aidtransparency homepage contains two news articles.
        """
        xpath = '//*[@id="home-featured"]/div/article'
        req = self.loaded_request_from_test_name(target_request)

        assert len(utility.locate_xpath_result(req, xpath)) == 2
