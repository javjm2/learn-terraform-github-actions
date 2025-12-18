import time
import pytest


def test_get_all_items(custom_requests, base_url, api_response_error):
    response = custom_requests().get(f"{base_url}/api/items")
    assert response.status_code == 200, api_response_error(response)


def test_add_todo_item(custom_requests, base_url, api_response_error):
    response = custom_requests().post(f"{base_url}/api/items", json={"name": "test"})
    assert response.status_code == 200, api_response_error(response)