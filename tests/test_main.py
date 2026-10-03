from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate() -> None:
    response = client.get("/calculate", params={"a": 10, "b": 20})

    assert response.status_code == 200
    assert response.json() == {"a": 10.0, "b": 20.0, "result": 30.0}


def test_statistics() -> None:
    response = client.post("/statistics", json={"values": [1, 2, 3, 4, 5]})

    assert response.status_code == 200
    assert response.json() == {"count": 5, "mean": 3.0, "min": 1.0, "max": 5.0}


def test_statistics_rejects_empty_list() -> None:
    response = client.post("/statistics", json={"values": []})

    assert response.status_code == 422


def test_calculate_rejects_invalid_input() -> None:
    response = client.get("/calculate", params={"a": "not-a-number", "b": 2})

    assert response.status_code == 422


def test_openapi_documentation_is_available() -> None:
    response = client.get("/docs")

    assert response.status_code == 200
    assert "Swagger UI" in response.text
