import pytest
from web_test_base import *

class TestGlobalConsistency(WebTestBase):
    requests_to_load = {
        'IATI Registry - Homepage': {
            'url': 'https://iatiregistry.org/'
        }
        , 'IATI Registry - Activity Dataset Page': {
            'url': 'https://iatiregistry.org/dataset?q=&filetype=Activity'
        }
        , 'IATI Registry - Organisation Dataset Page': {
            'url': 'https://iatiregistry.org/dataset?q=&filetype=Organisation'
        }
        , 'IATI Registry - organization Dataset Page': {
            'url': 'https://iatiregistry.org/dataset?q=&filetype=organization'
        }
        , 'IATI Dashboard - Homepage': {
            'url': 'http://dashboard.iatistandard.org/'
        }
        , 'IATI Dashboard - Activities Page': {
            'url': 'http://dashboard.iatistandard.org/activities.html'
        }
        , 'IATI Dashboard - Files Page': {
            'url': 'http://dashboard.iatistandard.org/files.html'
        }
        , 'IATI Dashboard - Publisher Page': {
            'url': 'http://dashboard.iatistandard.org/publishers.html'
        }
        , 'Datastore API - Activity Count': {
            'url': 'http://datastore.iatistandard.org/api/1/access/activity.xml?limit=0'
            , 'min_response_size': 300
        }
    }

    def test_activity_count_consistency(self):
        """
        Test to ensure the activity count is consistent across various
        locations that display this value.
        """
        dash_home_req = self.loaded_request_from_test_name('IATI Dashboard - Homepage')
        dash_activities_req = self.loaded_request_from_test_name('IATI Dashboard - Activities Page')
        datastore_api_req = self.loaded_request_from_test_name('Datastore API - Activity Count')
        dash_home_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a'
        dash_home_unique_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a'
        dash_activities_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div/div[1]/h3/span[1]'
        dash_activities_unique_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[2]/div/div[1]/h3/span[1]'
        datastore_api_xpath = '//result/iati-activities/query/total-count'
        min_activity_count = 550000
        max_datastore_disparity = 0.1

        dash_home_act_count = utility.get_single_int_from_xpath(dash_home_req, dash_home_xpath)
        dash_home_unique_act_count = utility.get_single_int_from_xpath(dash_home_req, dash_home_unique_xpath)
        dash_activities_act_count = utility.get_single_int_from_xpath(dash_activities_req, dash_activities_xpath)
        dash_activities_unique_act_count = utility.get_single_int_from_xpath(dash_activities_req, dash_activities_unique_xpath)
        datastore_api_act_count = utility.get_single_int_from_xpath(datastore_api_req, datastore_api_xpath)

        assert dash_home_act_count >= min_activity_count
        assert dash_home_unique_act_count >= min_activity_count
        assert dash_activities_act_count >= min_activity_count
        assert dash_activities_unique_act_count >= min_activity_count
        assert datastore_api_act_count >= min_activity_count

        assert dash_home_act_count == dash_activities_act_count
        assert dash_home_unique_act_count == dash_activities_unique_act_count
        assert dash_home_act_count >= dash_home_unique_act_count
        assert dash_activities_act_count >= dash_activities_unique_act_count

        assert (datastore_api_act_count >= dash_home_unique_act_count * (1 - max_datastore_disparity)) and (datastore_api_act_count <= dash_home_unique_act_count * (1 + max_datastore_disparity))

    def test_activity_dataset_count_consistency(self):
        """
        Test to ensure the dataset count is consistent across various
        locations that display this value.
        """
        registry_file_req = self.loaded_request_from_test_name('IATI Registry - Activity Dataset Page')
        dash_home_req = self.loaded_request_from_test_name('IATI Dashboard - Homepage')
        dash_files_req = self.loaded_request_from_test_name('IATI Dashboard - Files Page')
        registry_xpath = '//*[@id="content"]/div[3]/div/section[1]/div[1]/form/h2'
        dash_home_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[1]/a'
        dash_files_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div/div[1]/h3/span[1]'
        min_file_count = 4100
        max_registry_disparity = 0.025

        registry_file_count = utility.get_single_int_from_xpath(registry_file_req, registry_xpath)
        dash_home_file_count = utility.get_single_int_from_xpath(dash_home_req, dash_home_xpath)
        dash_files_count = utility.get_single_int_from_xpath(dash_files_req, dash_files_xpath)

        assert registry_file_count >= min_file_count
        assert dash_home_file_count >= min_file_count
        assert dash_files_count >= min_file_count

        assert dash_home_file_count == dash_files_count
        assert (registry_file_count >= dash_files_count * (1 - max_registry_disparity)) and (registry_file_count <= dash_files_count * (1 + max_registry_disparity))

    def test_organisation_dataset_count_consistency(self):
        """
        Test to ensure the dataset count is consistent across various
        locations that display this value.
        """
        registry_file_s_req = self.loaded_request_from_test_name('IATI Registry - Organisation Dataset Page')
        registry_file_z_req = self.loaded_request_from_test_name('IATI Registry - organization Dataset Page')
        dash_home_req = self.loaded_request_from_test_name('IATI Dashboard - Homepage')
        dash_files_req = self.loaded_request_from_test_name('IATI Dashboard - Files Page')
        registry_xpath = '//*[@id="content"]/div[3]/div/section[1]/div[1]/form/h2'
        dash_home_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[1]/a'
        dash_files_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[2]/div/div[1]/h3/span[1]'
        min_file_count = 350
        max_registry_disparity = 0.05

        registry_file_count = utility.get_single_int_from_xpath(registry_file_s_req, registry_xpath) + utility.get_single_int_from_xpath(registry_file_z_req, registry_xpath)
        dash_home_file_count = utility.get_single_int_from_xpath(dash_home_req, dash_home_xpath)
        dash_files_count = utility.get_single_int_from_xpath(dash_files_req, dash_files_xpath)

        assert registry_file_count >= min_file_count
        assert dash_home_file_count >= min_file_count
        assert dash_files_count >= min_file_count

        assert dash_home_file_count == dash_files_count
        assert (registry_file_count >= dash_files_count * (1 - max_registry_disparity)) and (registry_file_count <= dash_files_count * (1 + max_registry_disparity))

    def test_publisher_count_consistency(self):
        """
        Test to ensure the publisher count is consistent across various
        locations that display this value.
        """
        registry_home_req = self.loaded_request_from_test_name('IATI Registry - Homepage')
        dash_home_req = self.loaded_request_from_test_name('IATI Dashboard - Homepage')
        dash_publishers_req = self.loaded_request_from_test_name('IATI Dashboard - Publisher Page')
        registry_xpath = '//*[@id="home-icons"]/div/div[2]/div/a/strong'
        dash_home_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[1]/a'
        dash_pub_xpath = '//*[@id="wrap"]/div[2]/div[2]/div[1]/div/div[1]/h3/span[1]'
        min_publisher_count = 480
        max_registry_disparity = 0.01

        registry_pub_count = utility.get_single_int_from_xpath(registry_home_req, registry_xpath)
        dash_home_pub_count = utility.get_single_int_from_xpath(dash_home_req, dash_home_xpath)
        dash_pub_count = utility.get_single_int_from_xpath(dash_publishers_req, dash_pub_xpath)

        assert registry_pub_count >= min_publisher_count
        assert dash_home_pub_count >= min_publisher_count
        assert dash_pub_count >= min_publisher_count
        assert dash_home_pub_count == dash_pub_count

        assert (registry_pub_count >= dash_pub_count * (1 - max_registry_disparity)) and (registry_pub_count <= dash_pub_count * (1 + max_registry_disparity))
