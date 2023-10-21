import json
import os

import pytest
from mock import patch


@pytest.fixture()
def app_client():
    os.environ["APP_MODE"] = "TESTING"
    from main import app

    yield app.test_client()


@patch(
    "core.infra.repository.fake_employee_repository.FakeEmployeeRepository.get_employee_by_id"
)
def test_get_api_employee_by_id(mock, app_client):
    mock.return_value = {
        "id": 15,
        "name": "Paulo",
        "cpf": "38000966093",
        "gender": "Masculino",
        "gender_id": 1,
    }
    response = app_client.get(f"/employee/{mock.return_value['id']}")
    assert json.loads(response.data)["id"] == mock.return_value["id"]

    mock.return_value = None
    response = app_client.get("/employee/15")
    assert response.status_code == 404


@patch(
    "core.infra.repository.fake_employee_repository.FakeEmployeeRepository.get_employees"
)
def test_get_api_employees(mock, app_client):
    mock.return_value = [
        {
            "id": 15,
            "name": "Paulo",
            "cpf": "38000966093",
            "gender": "Masculino",
            "gender_id": 1,
        },
        {
            "id": 14,
            "name": "Maria",
            "cpf": "38000966093",
            "gender": "Feminino",
            "gender_id": 2,
        },
    ]
    response = app_client.get("/employee")
    # # check the status code of the response
    assert json.loads(response.data) == mock.return_value


@patch(
    "core.infra.repository.fake_employee_repository.FakeEmployeeRepository.create_employee"
)
def test_create_employee(mock, app_client):
    body = {
        "name": "string",
        "cpf": "18539421038",
        "gender_id": 2,
        "phone": 33081592,
        "email": "email@email.com",
        "CEP": 40850000,
        "address": "rua",
        "address_number": 13,
    }
    mock.return_value = None
    response = app_client.post(
        "/employee", data=json.dumps(body), content_type="application/json"
    )
    # # check the status code of the response
    assert response.status_code == 201

    body = {
        "name": "string",
        "cpf": "11304667890",
        "gender_id": 2,
        "phone": 33081592,
        "email": "email@email.com",
        "CEP": 40850000,
        "address": "rua",
        "address_number": 13,
    }
    mock.return_value = None
    response = app_client.post(
        "/employee", data=json.dumps(body), content_type="application/json"
    )
    # # check the status code of the response
    assert response.status_code == 400
