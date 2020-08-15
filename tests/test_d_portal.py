from web_test_base import WebTestBase


class TestDPortal(WebTestBase):
    """
    Test D-Portal (d-portal.org)
    """
    requests_to_load = {
        'D-Portal Homepage': {
            'url': 'http://d-portal.org/',
            'min_response_size': 1100
        }
    }
