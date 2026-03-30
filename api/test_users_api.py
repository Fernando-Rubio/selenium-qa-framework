from api.api_client import APIClient

client = APIClient()


def test_get_users():
     response = client.get_users()

     assert response.status_code == 200
     json_data = response.json()

     assert "users" in json_data
     assert len(json_data["users"]) > 0

def test_create_user():
     payload = {
          "firstName":"Fernando", 
          "job":"QA Engineer"
          }
     response = client.create_user(payload)

     assert response.status_code == 201

     json_data = response.json()

     assert json_data["firstName"] == "Fernando"