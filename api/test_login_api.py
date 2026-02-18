from api.api_client import APIClient
import pytest

client = APIClient()

@pytest.mark.parametrize("username, password, expected_status",[("emilys", "emilyspass", 200), ("emilys", "wrongpassword", 400), ("wronguser", "emilyspass", 400)])
def test_login_api(username, password, expected_status):
    response = client.login(username, password)
    assert response.status_code == expected_status

    if expected_status == 200:
        json_data = response.json()
        assert "accessToken" in json_data
        assert "id" in json_data
        assert "email" in json_data