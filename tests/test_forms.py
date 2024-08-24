import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_calculate_deposit_valid_input(client):
    response = client.post(
        "/api/calculate_deposit",
        json={"date": "01.01.2024", "amount": 10000, "periods": 3, "rate": 6.0},
    )

    assert response.status_code == 200
    json_data = response.get_json()
    assert "2024-01-01" in json_data
    assert json_data["2024-01-01"] == 10050.0


def test_calculate_deposit_invalid_date_format(client):
    response = client.post(
        "/api/calculate_deposit",
        json={"date": "2024.01.01", "amount": 10000, "periods": 3, "rate": 6.0},
    )

    assert response.status_code == 400
    json_data = response.get_json()
    assert "date" in json_data["errors"]
    assert "Invalid date format" in json_data["errors"]["date"][0]


def test_calculate_deposit_missing_fields(client):
    response = client.post(
        "/api/calculate_deposit", json={"date": "01.01.2024", "amount": 10000}
    )

    assert response.status_code == 400
    json_data = response.get_json()
    assert "periods" in json_data["errors"]
    assert "rate" in json_data["errors"]


def test_calculate_deposit_out_of_range(client):
    response = client.post(
        "/api/calculate_deposit",
        json={
            "date": "01.01.2024",
            "amount": 5000000,  # Вне пределов
            "periods": 3,
            "rate": 6.0,
        },
    )

    assert response.status_code == 400
    json_data = response.get_json()
    assert "amount" in json_data["errors"]
    assert (
        "Number must be between 10000 and 3000000" in json_data["errors"]["amount"][0]
    )
