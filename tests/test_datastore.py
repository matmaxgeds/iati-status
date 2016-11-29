import pytest
from web_test_base import *

class TestIATIDatastore(WebTestBase):
    requests_to_load = {
        'Datastore Homepage': {
            'url': 'http://datastore.iatistandard.org/'
        },
        'Datastore download: csv': {
            'url': 'http://dev.datastore.iatistandard.org/api/1/access/activity.csv'
        },
        'Datastore download: xml': {
            'url': 'http://datastore.iatistandard.org/api/1/access/activity.xml'
        },
        'Datastore download: json': {
            'url': 'http://datastore.iatistandard.org/api/1/access/activity.json'
        },
    }

    @pytest.mark.parametrize("target_request", ["Datastore Homepage"])
    def test_contains_links(self, target_request):
        """
        Test that each page contains links to the defined URLs.
        """
        loaded_request = self.loaded_request_from_test_name(target_request)
        result = utility.get_links_from_page(loaded_request)

        assert "http://iatiregistry.org/" in result

    @pytest.mark.parametrize("content_type", ["application/xml", "application/json", "text/csv"])
    def test_api_output_filetype(self, content_type):
        """
        Test that API calls return data in the expected filetypes.

        The test is conducted based upon the data returned in the request
        headers["content-type"]. For example, 'application/xml; charset=utf-8'
        """
        file_extenstion = content_type.split("/")[1]
        loaded_request = self.loaded_request_from_test_name("Datastore download: {}".format(file_extenstion))

        result = loaded_request.headers["content-type"]

        assert result.startswith(content_type)
