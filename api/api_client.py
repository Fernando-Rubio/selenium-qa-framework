import requests
from config.settings import Config

class APIClient():
    def __init__(self):
        self.base_url = Config.get_base_url()
    def login(self, username, password):
        return requests.post(f"{self.base_url}/auth/login", json={"username": username, "password": password})
    