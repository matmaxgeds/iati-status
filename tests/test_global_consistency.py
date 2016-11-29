import pytest
from web_test_base import *

class TestGlobalConsistency(WebTestBase):
    requests_to_load = {
        'IATI Registry': {
            'url': 'https://iatiregistry.org/'
        }
        , 'IATI Dashboard - Homepage': {
            'url': 'http://dashboard.iatistandard.org/'
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

    def test_publisher_count_consistency(self):
        """
        Test to ensure the publisher count is consistent across various
        locations that display this data.
        """
        registry_homepage_req = self.loaded_request_from_test_name('IATI Registry')
        dashboard_homepage_req = self.loaded_request_from_test_name('IATI Dashboard - Homepage')
        dashboard_publishers_req = self.loaded_request_from_test_name('IATI Dashboard - Publisher Page')
        registry_xpath = '//*[@id="home-icons"]/div/div[2]/div/a/strong'
        dashboard_home_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/a'
        dashboard_pub_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div/div[1]/h3/span[1]'
        min_publisher_count = 480
        max_registry_disparity = 0.01

        registry_pub_count = utility.get_single_int_from_xpath(registry_homepage_req, registry_xpath)
        dashboard_home_pub_count = utility.get_single_int_from_xpath(dashboard_homepage_req, dashboard_home_xpath)
        dashboard_pub_count = utility.get_single_int_from_xpath(dashboard_publishers_req, dashboard_pub_xpath)

        assert registry_pub_count >= min_publisher_count
        assert dashboard_home_pub_count >= min_publisher_count
        assert dashboard_pub_count >= min_publisher_count
        assert dashboard_home_pub_count == dashboard_pub_count
        assert (registry_pub_count >= dashboard_pub_count * (1 - max_registry_disparity)) and (registry_pub_count <= dashboard_pub_count * (1 + max_registry_disparity))
