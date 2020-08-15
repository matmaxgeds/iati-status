"""A module to test critical access to aidstream hosted datasets."""
import pytest
from lxml import etree
from web_test_base import WebTestBase


class TestAidstream(WebTestBase):
    """Setup URLs for tests."""

    requests_to_load = {
        'Aidstream homepage': {
            'url': 'https://aidstream.org/'
        },
        'Aidstream hosted dataset 1': {
            'url': 'https://aidstream.org/files/xml/abaseen-activities.xml'
        },
        'Aidstream hosted dataset 2': {
            'url': 'https://aidstream.org/files/xml/ageintl-activities.xml'
        },
        'Aidstream hosted dataset 3': {
            'url': 'http://aidstream.org/files/xml/tfacmalawi-activities.xml'
        }
    }

    @pytest.mark.parametrize("target_request", ["Aidstream hosted dataset 1",
                                                "Aidstream hosted dataset 2",
                                                "Aidstream hosted dataset 3"])
    def test_load_aidstream_datasets(self, target_request):
        """Test that aidstream sample datasets are live."""
        req = self.loaded_request_from_test_name(target_request)

        iati_activity_xpath = 'iati-activity'
        tree = etree.fromstring(req.text)
        result = tree.xpath(iati_activity_xpath)
        assert len(result) >= 1
