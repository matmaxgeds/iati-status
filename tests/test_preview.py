import pytest
from web_test_base import *

class TestIATIPreview(WebTestBase):
    requests_to_load = {
        'IATI Preview': {
            'url': 'http://preview.iatistandard.org/'
        }
    }

    def test_contains_links(self, loaded_request):
        """
        Test that each page contains links to the defined URLs.
        """
        result = utility.get_links_from_page(loaded_request)

        assert "http://www.iatistandard.org/" in result

    @pytest.mark.parametrize("target_request", ["IATI Preview"])
    def test_xml_web_address_form_presence(self, target_request):
        """
        Test that there is a form to enter a URL of a valid XML file on the Preview Tool.
        """
        req = self.loaded_request_from_test_name(target_request)
        form_xpath = '//*[@id="main"]/div/div/div[1]/div/form'
        form_action_xpath = '//*[@id="main"]/div/div/div[1]/div/form/@action'
        form_method_xpath = '//*[@id="main"]/div/div/div[1]/div/form/@method'
        input_xpath = '//*[@id="url"]'
        button_xpath = '//*[@id="main"]/div/div/div[1]/div/form/div/div/span/button'

        forms = utility.locate_xpath_result(req, form_xpath)
        form_action = utility.locate_xpath_result(req, form_action_xpath)
        form_method = utility.locate_xpath_result(req, form_method_xpath)
        form_inputs = utility.locate_xpath_result(req, input_xpath)
        form_buttons = utility.locate_xpath_result(req, button_xpath)

        assert len(forms) == 1
        assert form_action == ['index.php']
        assert form_method == ['get']
        assert len(form_inputs) == 1
        assert len(form_buttons) == 1
