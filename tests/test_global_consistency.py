import pytest
from web_test_base import *

class TestGlobalConsistency(WebTestBase):
    requests_to_load = {
        'IATI Registry': {
            'url': 'https://iatiregistry.org/'
        }
        , 'IATI Dashboard - Publisher Page': {
            'url': 'http://dashboard.iatistandard.org/publishers.html'
        }
        , 'IATI Dashboard - Activities Page': {
            'url': 'http://dashboard.iatistandard.org/activities.html'
        }
        , 'Datastore API - Activity Count': {
            'url': 'http://datastore.iatistandard.org/api/1/access/activity.xml?limit=0'
            , 'min_response_size': 300
        }
    }
