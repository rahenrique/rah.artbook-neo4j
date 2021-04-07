import pytest
import requests
import uuid


class TestArtworks:
    @pytest.fixture
    def my_uuid(self):
        """
        Returns a controlled uuid, providing a namespace and a name
        """
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, self.__class__.__name__))


    def test_post_creates_new_artwork(self, my_uuid):
        new_artwork = {"uuid":my_uuid, "title":"Test Artwork", "creation":"1937-01-01", "techniques":["Pintura", "Óleo sobre tela"]}
        response = requests.post("http://0.0.0.0:5000/api/artworks/", data=new_artwork)
        uuid = response.json()

        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/json"
        assert uuid == my_uuid


    def test_get_single_return_an_artwork(self, my_uuid):
        response = requests.get("http://0.0.0.0:5000/api/artworks/"+my_uuid)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

        assert response_body["uuid"] == my_uuid
        assert response_body["title"] == "Test Artwork"
        assert response_body["creation"] == "1937-01-01"
        # assert response_body["techniques"] == ["Pintura", "Óleo sobre tela"]
