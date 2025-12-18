import os

import pytest
import requests
from utils.config import Config

config = Config()
@pytest.fixture(scope="session")
def custom_requests():
    def wrap():
        return config.config_requests()

    return wrap


@pytest.fixture
def base_url():
    return config.base_url


@pytest.fixture
def api_response_error():
    def wrap(response):
        return f"Actual response {response.status_code}: {response.text}"

    return wrap
