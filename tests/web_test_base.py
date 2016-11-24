import requests
import pytest

class WebTestBase:
    urls = ["http://iatiregistry.org"]
    expected_link = 3
    loaded_urls = dict()
    num_urls = len(urls)

    def display_urls(self):
        return self.urls

    @classmethod
    def setup_class(cls):
        # import pdb;pdb.set_trace()
        for url in cls.urls:
            result = requests.get(url)
            cls.loaded_urls[url] = result
        cls.num_urls = len(cls.urls)

    def pytest_generate_tests(cls, metafunc):
        if 'nxt_req' in metafunc.fixturenames:
            metafunc.parametrize("nxt_req", cls.urls)

    def loaded_request(self, idx):
        return self.loaded_urls[self.urls[idx]]

    # @pytest.fixture(scope="class", params=urls)
    # def load_urls(self, request):
        # result = requests.get(request.param)
        # return result

    @pytest.mark.parametrize("idx", range(0, num_urls), scope="class")
    def test_url_check(self, idx):
        assert self.num_urls == 3

    def test_expected_link(self):
        assert self.expected_link == 4

    def test_num_urls(self):
        assert self.num_urls == 2

    def test_correct_url(self, nxt_req):
        assert len(self.urls) == 2
        assert nxt_req == 8
