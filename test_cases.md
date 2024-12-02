# API MANUAL TEST CASES

## Test Case 1: Get list of inventory devices
- **Test ID:** TC_GET_001  
- **Description:** Verify that the API returns all devices available in the inventory.  
- **Steps:**  
  1. Send a `GET` request to the endpoint `http://localhost:8080/inventory/devices`.  
- **Expected Result:**  
  - Status code: `200 OK`.  
  - Response contains a list of devices with at least one element.  
- **Actual Result:** 
  - Actual Result: The response returns list of all devices in the system.


## Test Case 2: Add new device to inventory
- **Test ID:** TC_PUT_002  
- **Description:** Verify that a new device can be added to the inventory.  
- **Steps:**  
  1. Send a `PUT` request to the endpoint `http://localhost:8080/inventory/devices` with the following JSON body:
  {
      "body": {
          "id": "TEST",
          "model": "TEST_DEVICE"
      },
      "status_code": 200
  }
- **Expected Result:**  
  - Status code: `200 OK`.  
  - Response contains the newly added device with "id": "TEST" and "model": "TEST_DEVICE".
- **Actual Result:**
  - The device is added successfully.


## Test Case 3: Add device to inventory without populating required body
- **Test ID:** TC_POST_003
- **Description:** Verify that adding a device with missing required fields fails.
- **Steps:**
  1. Send a `PUT` request to the endpoint `http://localhost:8080/inventory/devices` with the following JSON body:
  {
      "body": {
          "id": "",
          "model": ""
      },
      "status_code": 405
  }
- **Expected Result:**
  - Status code: `405 Method Not Allowed`.
  - Device is not added to the inventory.
- **Actual Result:**
  - Fail - Device is not added.


### Test Case 4: Update existing device
- **Test ID:** TC_PUT_004
- **Description:** Verify that an existing device can be updated with new details.
- **Steps:**
  1. Send a PUT request to the endpoint `http://localhost:8080/inventory/devices` with the following JSON body:
    {
        "body": {
            "id": "TEST",
            "model": "TEST_MODEL_UPDATED"
        },
        "status_code": 200
    }
    ```
- **Expected Result:**
  - Status code: `200 OK`.
  - Response contains the updated device with `"id": "TEST"` and `"model": "TEST_MODEL_UPDATED"`.
- **Actual Result:**
  - The device is updated successfully.


### Test Case 5: Update device that does not exist
- **Test ID:** TC_PUT_005
- **Description:** Verify that attempting to update a non-existing device fails.
- **Steps:**
  1. Send a PUT request to the endpoint `http://localhost:8080/inventory/devices` with the following JSON body:
    {
        "body": {
            "id": "NONE",
            "model": "SHOULD_NOT_WORK"
        },
        "status_code": 404
    }
    ```
- **Expected Result:**
  - Status code: `404 Not Found`.
  - Device is not updated, and an appropriate error message is returned.
- **Actual Result:**
  - Fail - Device is successfully updated.


### Test Case 6: Get device details by ID
- **Test ID:** TC_GET_006
- **Description:** Verify that details of a specific device can be retrieved using its ID.
- **Steps:**
  1. Send a GET request to the endpoint `http://localhost:8080/inventory/devices/TEST`.
- **Expected Result:**
  - Status code: `200 OK`.
  - Response contains device details with `"id": "TEST"`.
- **Actual Result:**
  - Method is not implemented - Error code 404.




