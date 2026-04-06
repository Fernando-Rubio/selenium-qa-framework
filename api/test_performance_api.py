from api.api_client import APIClient

client = APIClient()

def test_users_response_time():
    response = client.get_users()

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3