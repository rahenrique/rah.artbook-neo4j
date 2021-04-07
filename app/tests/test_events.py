import pytest
import requests
import uuid


class TestEvents:
    @pytest.fixture
    def my_uuid(self):
        """
        Returns a controlled uuid, providing a namespace and a name
        """
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, self.__class__.__name__))


    def test_post_creates_new_event(self, my_uuid):
        new_event = {"uuid":my_uuid, "title":"Event With Given UUID", "start":"2021-01-01", "end":"2021-02-01"}
        response = requests.post("http://0.0.0.0:5000/api/events/", data=new_event)
        uuid = response.json()

        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert uuid == my_uuid


    def test_get_single_return_an_event(self, my_uuid):
        response = requests.get("http://0.0.0.0:5000/api/events/"+my_uuid)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

        assert response_body["uuid"]  == my_uuid
        assert response_body["title"] == "Event With Given UUID"
        assert response_body["start"] == "2021-01-01"
        assert response_body["end"]   == "2021-02-01"


    def test_get_return_list_of_events(self, my_uuid):
        response = requests.get("http://0.0.0.0:5000/api/events/")
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

        assert response_body[0]["uuid"] is not None
        assert response_body[0]["title"] is not None
        assert response_body[0]["start"] is not None
        assert response_body[0]["end"] is not None


    def test_put_updates_an_event(self, my_uuid):
        updated_event = {"title":"Updated Event", "start":"2022-01-01", "end":"2022-02-01"}
        response = requests.put("http://0.0.0.0:5000/api/events/"+my_uuid, data=updated_event)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        
        assert response_body["uuid"]  == my_uuid
        assert response_body["title"] == "Updated Event"
        assert response_body["start"] == "2022-01-01"
        assert response_body["end"]   == "2022-02-01"


    def test_patch_updates_partially_an_event(self, my_uuid):
        updated_event = {"title":"Updated Again"}
        response = requests.patch("http://0.0.0.0:5000/api/events/"+my_uuid, data=updated_event)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        
        assert response_body["uuid"]  == my_uuid
        assert response_body["title"] == "Updated Again"
        assert response_body["start"] == "2022-01-01"
        assert response_body["end"]   == "2022-02-01"


    def test_delete_removes_an_event(self, my_uuid):
        response = requests.delete("http://0.0.0.0:5000/api/events/"+my_uuid)
        assert response.status_code == 204


    def test_full_crud_without_providing_uuid(self):
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
