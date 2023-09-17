import pytest
from swagger_page import SwaggerPage


class TestSwagger():

    @pytest.mark.parametrize("login, password, result_code",
                             [("loginDemo", "!11asswordDemo", 201),
                              ("1loginDemo", "!11asswordDemo", 201),
                              ("loginDemo", "!11asswordDemo", 406),
                              ("loginDemo11", "asswordemo", 400)])
    def test_new_user(self, login, password, result_code):
        swagger = SwaggerPage()
        response = swagger.post_user(login, password)
        assert response.status_code == result_code

    @pytest.mark.parametrize("login, password, status",
                             [("loginDemo", "!11asswordDemo", "Success"),
                              ("loginDeo", "!11asswordDemo", "Failed")])
    def test_generate_token(self, login, password, status):
        swagger = SwaggerPage()
        response = swagger.post_generate_token(login, password)
        assert response.status_code == 200 and response.json()["status"] == status

    @pytest.mark.parametrize("login, password, status",
                             [("loginDemo", "!11asswordDemo", True),
                              ("1loginDemo", "!11asswordDemo", False)])
    def test_is_authorized(self, login, password, status):
        swagger = SwaggerPage()
        response = swagger.post_authorized(login, password)
        print(response.json())
        assert response.status_code == 200 and response.json() == status

    @pytest.mark.parametrize("login, password",
                             [("loginDemo11", "!11asswordDemo"),
                              ("1loginDemo111", "!11asswordDemo")])
    def test_get_user(self, login, password):
        swagger = SwaggerPage()
        response = swagger.post_user(login, password)
        uuid = response.json()["userID"]
        response = swagger.get_user(login, password, uuid)
        assert response.status_code == 200 and response.json()['username'] == login

    @pytest.mark.parametrize("login, password",
                             [("1loginDemo11", "!11asswordDemo"),
                              ("11loginDemo111", "!11asswordDemo")])
    def test_delete_user(self, login, password):
        swagger = SwaggerPage()
        response = swagger.post_user(login, password)
        uuid = response.json()["userID"]
        response = swagger.delete_user(login, password, uuid)
        assert response.status_code == 204
