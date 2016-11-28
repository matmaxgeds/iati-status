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
        parent_xpath = '//*[@id="home-featured"]/div/article'
        title1_xpath = '//*[@id="home-featured"]/div/article[1]/div[2]/h2/a'
        title2_xpath = '//*[@id="home-featured"]/div/article[2]/div[2]/h2/a'
        summary1_xpath = '//*[@id="home-featured"]/div/article[1]/div[2]'
        summary2_xpath = '//*[@id="home-featured"]/div/article[2]/div[2]'
        min_title_length = 10
        max_title_length = 100
        min_summary_length = 40
        max_summary_length = 250

        req = self.loaded_request_from_test_name(target_request)

        assert len(utility.locate_xpath_result(req, parent_xpath)) == 2
        assert max_title_length > len(utility.get_joined_text_from_xpath(req, title1_xpath)) > min_title_length
        assert max_title_length > len(utility.get_joined_text_from_xpath(req, title2_xpath)) > min_title_length
        assert max_summary_length > len(utility.get_joined_text_from_xpath(req, summary1_xpath).strip()) > min_summary_length
        assert max_summary_length > len(utility.get_joined_text_from_xpath(req, summary2_xpath).strip()) > min_summary_length
