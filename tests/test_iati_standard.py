import pytest
from web_test_base import *

class TestIATIStandard(WebTestBase):
    urls_to_get = [
        "http://iatistandard.org/"
        , "http://www.iatistandard.org/"
        , "http://iatistandard.org/202/guidance/how-to-publish/prepare-your-org/"
        , "http://iatistandard.org/202/organisation-standard/summary-table/"
        , "http://iatistandard.org/202/schema/"
        , "http://iatistandard.org/105/developer/"
        , "http://iatistandard.org/105/developer/xquery/"
        , "http://iatistandard.org/105/activity-standard/iati-activities/iati-activity/contact-info/"
        , "http://iatistandard.org/201/"
    ]

    def test_locate_xpath_content(self, loaded_request):
        """
        Tests that a page contains a html element
        """
        result = self._get_links_from_page(loaded_request)

        assert "http://iatistandard.org" in result
        assert "http://www.aidtransparency.net/" in result
        assert "http://iatiregistry.org" in result
