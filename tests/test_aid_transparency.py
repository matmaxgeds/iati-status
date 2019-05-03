from web_test_base import WebTestBase


class TestAidTransparency(WebTestBase):
    requests_to_load = {
        'AidTransparency Homepage - HTTPS - no www': {
            'url': 'https://aidtransparency.net/'
        },
        'AidTransparency Homepage - HTTPS - with www': {
            'url': 'https://www.aidtransparency.net/'
        },
        'AidTransparency Homepage - HTTP - no www': {
            'url': 'http://aidtransparency.net/'
        },
        'AidTransparency Homepage - HTTP - with www': {
            'url': 'http://www.aidtransparency.net/'
        },
        'AidTransparency Random Page': {
            'url': 'https://www.aidtransparency.net/governance/secretariat/iati-technical-team'
        }
    }

    def test_homepage_redirects_to_https_on_iatistandard_org(self, loaded_request):
        """
        Test that a request made to aidtransparency.net is redirected to iatistandard.org
        """
        assert 'https://iatistandard.org/' in loaded_request.url
