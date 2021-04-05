import pytest
import requests


class TestEvent:
    def test_get_index_check_status_code_equals_200(c):
        response = requests.get("http://0.0.0.0:5000/api/events/")
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response_body[0]["title"] is not None


