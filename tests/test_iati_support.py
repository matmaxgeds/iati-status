from web_test_base import WebTestBase


class TestIATISupport(WebTestBase):
    requests_to_load = {
        'support.iatistandard.org': {
            'url': 'http://support.iatistandard.org'
        }
    }
