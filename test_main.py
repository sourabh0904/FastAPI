from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_add_numbers():
    response = client.post("/math/add", json={"a": 5, "b": 3}, headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_add_numbers_negative():
    response = client.post("/math/add", json={"a": -5, "b": 3} , headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 422  

def test_add_numbers_missing_field():
    response = client.post("/math/add", json={"a": 5} , headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 422  

def test_add_numbers_non_integer():
    response = client.post("/math/add", json={"a": "five", "b": 3}, headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 422  

def test_add_numbers_zero():
    response = client.post("/math/add", json={"a": 0, "b": 3} , headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 422  

def test_about_valid_name():
    response = client.get("/general/about/sourabh")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, sourabh!"}

def test_about_invalid_name():
    response = client.get("/general/about/123")
    assert response.status_code == 400 

def test_update_numbers():
    response = client.put("/math/update", json={"a": 10, "b": 20} , headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 200
    assert response.json() == {"a": 10, "b": 20}

def test_delete_numbers():
    response = client.request("DELETE" , "/math/delete", json={"a": 10, "b": 20} , headers={"x-api-key": "my-secret-key-12345"})
    assert response.status_code == 200
    assert response.json() == {"message": "Deleted numbers: a=10, b=20"}
    