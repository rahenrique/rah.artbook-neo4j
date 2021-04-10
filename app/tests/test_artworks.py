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


    def test_get_return_list_of_artworks(self, my_uuid):
        response = requests.get("http://0.0.0.0:5000/api/artworks/")
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"

        assert response_body[0]["uuid"] is not None
        assert response_body[0]["title"] is not None
        assert response_body[0]["creation"] is not None
        # assert response_body[0]["techniques"] is not None


    def test_put_updates_an_artwork(self, my_uuid):
        updated_artwork = {"title":"Updated Artwork", "creation":"2022-01-01", "techniques":["Pintura"]}
        response = requests.put("http://0.0.0.0:5000/api/artworks/"+my_uuid, data=updated_artwork)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        
        assert response_body["uuid"] == my_uuid
        assert response_body["title"] == "Updated Artwork"
        assert response_body["creation"] == "2022-01-01"
        # assert response_body["techniques"] == ["Pintura"]


    def test_patch_updates_partially_an_artwork(self, my_uuid):
        updated_artwork = {"title":"Updated Again"}
        response = requests.patch("http://0.0.0.0:5000/api/artworks/"+my_uuid, data=updated_artwork)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        
        assert response_body["uuid"]  == my_uuid
        assert response_body["title"] == "Updated Again"
        assert response_body["creation"] == "2022-01-01"
        # assert response_body["techniques"] == ["Pintura"]


    def test_delete_removes_an_artwork(self, my_uuid):
        response = requests.delete("http://0.0.0.0:5000/api/artworks/"+my_uuid)
        assert response.status_code == 204


    def test_full_crud_without_providing_uuid(self):
        """
        This test breaks the AAA (Arrange-Act-Assert) pattern intentionally!
        I just don't know how to control the generated UUID, to use the same identifier in other methods, 
        and separate the responsibilities of creation and deletion in different functions.
        """
        new_artwork = {"title":"Artwork With Auto UUID", "creation":"1937-01-01", "techniques":["Pintura", "Óleo sobre tela"]}
        response = requests.post("http://0.0.0.0:5000/api/artworks/", data=new_artwork)
        uuid = response.json()

        assert response.status_code == 201
        assert uuid is not None

        response = requests.delete("http://0.0.0.0:5000/api/artworks/"+uuid)
        assert response.status_code == 204

