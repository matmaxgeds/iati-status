from web_test_base import *
import pytest

class TestRegistry(WebTestBase):
    urls = ["http://iatistandard.org/", "http://aidtransparency.org/"]
    expected_link = 4

    # def load_urls(self, request):
        # return super(TestRegistry, self).load_urls(request)

    def test_urls(self):
        assert self.urls[0] == "http://iatistandard.org/"

    @pytest.mark.parametrize("idx", range(0, len(urls)), scope="class")
    def test_status(self, idx):
        request = self.loaded_request(idx)

        assert len(self.loaded_urls) == len(self.urls)
        assert request.status_code == 200
