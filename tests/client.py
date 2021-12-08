import deepdiff
import requests
import logging
from hamcrest import assert_that, equal_to

logging.basicConfig(level=logging.INFO)


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _build_url(self, url):
        logging.info(f'Request url: {self.base_url}/{url}')
        return f'{self.base_url}/{url}'

    def get(self, url, headers=None, cookies=None):
        return ApiResponse(self.session.get(self._build_url(url), headers=headers, cookies=cookies))

    def post(self, url, body, headers=None, cookies=None):
        return ApiResponse(self.session.post(self._build_url(url), json=body, headers=headers, cookies=cookies))

    def delete(self, url, headers=None, cookies=None):
        return ApiResponse(self.session.get(self._build_url(url), headers=headers, cookies=cookies))


# api response
class ApiResponse:
    def __init__(self, response):
        self._response = response

    def body(self):
        return self._response.json()

    def text(self):
        return self._response.text

    def check_status(self, status_code):
        logging.info('About to check ' + str(self._response.status_code))
        # assert_that(self._response.status_code, equal_to(status_code))
        assert self._response.status_code == status_code, \
            f'Status codes are different! Status code from response: {self._response.status_code}\n' \
            f' Expected status code: {status_code}'

    def exact_body(self, expected_body, ignore=None):
        resp = self.body()
        diff = deepdiff.DeepDiff(resp, expected_body, exclude_paths=ignore)
        if diff:
            logging.info(diff.to_json())
            assert_that(diff.to_json(), equal_to({}))
