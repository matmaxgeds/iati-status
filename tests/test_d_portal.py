import pytest
from web_test_base import *

class TestDPortal(WebTestBase):
    requests_to_load = {
        'D-Portal Homepage': {
            'url': 'http://d-portal.org/'
        }
    }
