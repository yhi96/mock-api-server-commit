from configuration import url, verify
import requests
import pytest


def test_https_get_request():

    url = "https://localhost:8443/inventory/devices"

    response = requests.get(url, verify=verify)
    
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"
    print(response.json())


def test_https_add_new_device_to_inventory():

    url = "https://localhost:8443/inventory/devices"

    send_data = {
    "body": {

        "id": "TEST",
        "model": "TEST_DEVICE"
    },
    "status_code": 200
}

    response = requests.put(url, json=send_data, verify=verify)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"

    response_data = response.json()
    model = response_data.get("new_body", {}).get('model')
    assert model == "TEST_DEVICE", f"The device name in the response, does not match the created device name {'model'}"


def test_https_add_device_to_inventory_without_populating_required_body():

    url = "https://localhost:8443/inventory/devices"

    send_data = {
    "body": {

        "id": "",
        "model": ""
    },
    "status_code": 405
}

    response = requests.post(url, json=send_data, verify=verify)

    assert response.status_code == 405, f"Response status code is not as expected, instead we got {response.status_code}"


def test_https_update_existing_device():

    url = "https://localhost:8443/inventory/devices"

    updated_data = {
    "body": {

        "id": "TEST",
        "model": "TEST_MODEL_UPDATED"
    },
    "status_code": 200
}

    response = requests.put(url, json=updated_data, verify=verify)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code['model']}"

    response_data = response.json()
    model = response_data.get("new_body", {}).get('model')
    assert model == "TEST_MODEL_UPDATED", f"Expected model was 'TEST_MODEL_UPDATED', but instead we got {'model'}"


def test_https_update_device_that_does_not_exist():

    url = "https://localhost:8443/inventory/devices"

    updated_data = {
    "body": {

        "id": "NONE",
        "model": "SHOULD_NOT_WORK"
    },
    "status_code": 404
}

    response = requests.put(url, json=updated_data,verify=verify)

    assert response.status_code == 404, f"Response status code is not as expected, instead we got {response.status_code}"
    # Bug described in same test, but using http in test_inventory.py


def test_https_get_device_details_by_id():

    url = "https://localhost:8443/inventory/devices/TEST"

    response = requests.get(url, verify=verify)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"
    # Not imlemented