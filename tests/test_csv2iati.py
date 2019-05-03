from web_test_base import WebTestBase


class TestCSV2IATI(WebTestBase):
    requests_to_load = {
        'CSV2IATI Homepage': {
            'url': 'http://csv2iati.iatistandard.org/',
            'min_response_size': 1500
        }
    }
