import requests


class SwaggerPage():

    def __init__(self):
        self.url = 'https://demoqa.com/Account/v1/'

    def post_authorized(self, user_name, password):
        data = {"userName": user_name, "password": password}
        response = requests.post(self.url + "Authorized", json=data)
        return response

    def post_generate_token(self, user_name, password):
        data = {"userName": user_name, "password": password}
        response = requests.post(self.url + "GenerateToken", json=data)
        return response

    def post_user(self, user_name, user_password):
        data = {"userName": user_name, "password": user_password}
        response = requests.post(self.url + "User", json=data)
        return response

    def delete_user(self, user_name, user_password, user_id):
        auth = requests.auth.HTTPBasicAuth(user_name, user_password)
        response = requests.delete(self.url + f"User/{user_id}", auth=auth)
        return response

    def get_user(self, user_name, user_password, user_id):
        auth = requests.auth.HTTPBasicAuth(user_name, user_password)
        response = requests.get(self.url + f"User/{user_id}", auth=auth)
        return response
