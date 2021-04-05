import pytest
import requests
import uuid


class TestEvents:
    @pytest.fixture
    def my_uuid(self):
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, 'event'))


    def test_post_creates_new_event_with_uuid(self, my_uuid):
        new_event = {"uuid":my_uuid, "title":"Event With Given UUID", "start":"2021-01-01", "end":"2021-02-01"}
        response = requests.post("http://0.0.0.0:5000/api/events/", data=new_event)
        uuid = response.json()

        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert uuid == my_uuid


    def test_get_list_check_event_has_fields(self, my_uuid):
        response = requests.get("http://0.0.0.0:5000/api/events/")
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

        assert response_body[0]["uuid"] is not None
        assert response_body[0]["title"] is not None
        assert response_body[0]["start"] is not None
        assert response_body[0]["end"] is not None


    def test_delete_event_with_uuid(self, my_uuid):
        response = requests.delete("http://0.0.0.0:5000/api/events/"+my_uuid)
        assert response.status_code == 204


    def test_post_creates_new_event_without_providing_uuid(self):
        """
        This test breaks the AAA (Arrange-Act-Assert) pattern intentionally!
        I just don't know how to control the generated UUID, to use the same identifier in other methods, 
        and separate the responsibilities of creation and deletion in different functions.
        """
        new_event = {"title":"Event With Auto UUID", "start":"2021-01-01", "end":"2021-02-01"}
        response = requests.post("http://0.0.0.0:5000/api/events/", data=new_event)
        uuid = response.json()

        assert response.status_code == 201
        assert uuid is not None

        response = requests.delete("http://0.0.0.0:5000/api/events/"+uuid)
        assert response.status_code == 204
