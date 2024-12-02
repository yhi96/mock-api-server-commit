import requests
import pytest

def test_get_list_of_inventory_devices():

    url = "http://localhost:8080/inventory/devices"

    response = requests.get(url)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"
    assert len(response.json()) > 0, "Response is not empty, it contains at least 1 element"

def test_add_new_device_to_inventory():

    url = "http://localhost:8080/inventory/devices"

    send_data = {
    "body": {

        "id": "TEST",
        "model": "TEST_DEVICE"
    },
    "status_code": 200
}

    response = requests.put(url, json=send_data)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"

    response_data = response.json()
    model = response_data.get("new_body", {}).get('model')
    assert model == "TEST_DEVICE", f"The device name in the response, does not match the created device name {'model'}"

def test_add_device_to_inventory_without_populating_required_body():

    url = "http://localhost:8080/inventory/devices"

    send_data = {
    "body": {

        "id": "",
        "model": ""
    },
    "status_code": 405
}

    response = requests.post(url, json=send_data)

    assert response.status_code == 405, f"Response status code is not as expected, instead we got {response.status_code}"

def test_update_existing_device():

    url = "http://localhost:8080/inventory/devices"

    updated_data = {
    "body": {

        "id": "TEST",
        "model": "TEST_MODEL_UPDATED"
    },
    "status_code": 200
}

    response = requests.put(url, json=updated_data)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code['model']}"

    response_data = response.json()
    model = response_data.get("new_body", {}).get('model')
    assert model == "TEST_MODEL_UPDATED", f"Expected model was 'TEST_MODEL_UPDATED', but instead we got {'model'}"

def test_update_device_that_does_not_exist():

    url = "http://localhost:8080/inventory/devices"

    updated_data = {
    "body": {

        "id": "NONE",
        "model": "SHOULD_NOT_WORK"
    },
    "status_code": 404
}

    response = requests.put(url, json=updated_data)

    assert response.status_code == 404, f"Response status code is not as expected, instead we got {response.status_code}"
    # Here it's not very clear what should be the behavior, but if we try to update existing device with it's ID, it gives 200 OK.
    # Response contains the updated body(with id: NONE and model: SHOULD_NOT_WORK), but then, if we try to run GET request go get,
    # the list of existing devices we get 404 NOT FOUND, but still the response in the console is the updated body
    # (with id: NONE and model: SHOULD_NOT_WORK) and the first GET LIST test does not pass anymore.

def test_get_device_details_by_id():

    url = "http://localhost:8080/inventory/devices/TEST"

    response = requests.get(url)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"
    # This functionallity is not implemented
    