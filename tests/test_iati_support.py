from web_test_base import WebTestBase


class TestIATISupport(WebTestBase):
    requests_to_load = {
        'IATI Support Landing Page': {
            'url': 'http://support.iatistandard.org/hc/en-us'
        }
    }
