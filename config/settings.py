import os

class Config:
    ENV = os.getenv("ENV", "dev")
    BASE_URL = {"dev": "https://dummyjson.com", "staging": "https://dummyjson.com", "prod": "https://dummyjson.com"}
    @classmethod
    def get_base_url(cls):
        return cls.BASE_URL.get(cls.ENV)