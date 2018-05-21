import pytest
from web_test_base import *

class TestCSV2IATI(WebTestBase):
    requests_to_load = {
        'CSV2IATI Homepage': {
            'url': 'http://csv2iati.iatistandard.org/'
        }
    }
