import requests
from config.settings import Config
from utils.logger import get_logger

class APIClient():
    def __init__(self):
        self.base_url = Config.get_base_url()
        self.logger = get_logger(__name__)

    def login(self, username, password):
        self.logger.info(f"Attempting login for user: {username}")
        response = requests.post(f"{self.base_url}/auth/login", json={"username": username, "password": password})
        self.logger.info(f"Response Status: {response.status_code}")
        return response
    
    def get_users(self):
        self.logger.info("Fetching users")
        response = requests.get(f"{self.base_url}/users")
        self.logger.info(f"Response Status: {response.status_code}")
        return response
    
    def create_user(self, payload):
        self.logger.info("Creating user")
        response = requests.post(f"{self.base_url}/users/add", json=payload)
        self.logger.info(f"Response Status: {response.status_code}")
        return response