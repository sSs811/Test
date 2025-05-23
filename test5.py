import pytest
import requests

BMC_URL = "https://localhost:2443"
USERNAME = "root"
PASSWORD = "0penBmc"

@pytest.fixture(scope="session")
def redfish_session():
    url = f"{BMC_URL}/redfish/v1/SessionService/Sessions"
    headers = {"Content-Type": "application/json"}
    data = {"UserName": USERNAME, "Password": PASSWORD}

    response = requests.post(url, headers=headers, json=data, verify=False)
    assert response.status_code == 201, "Auth failed"
    token = response.headers.get("X-Auth-Token")
    assert token is not None, "No token returned"

    session = requests.Session()
    session.headers.update({"X-Auth-Token": token})
    return session

def test_authentication(redfish_session):
    assert redfish_session.headers.get("X-Auth-Token") is not None
    
def test_get_system_info(redfish_session):
    url = f"{BMC_URL}/redfish/v1/Systems/system"
    response = redfish_session.get(url, verify=False)
    assert response.status_code == 200
    json_data = response.json()
    assert "Status" in json_data
    assert "PowerState" in json_data
import time

def test_power_on(redfish_session):
    url = f"{BMC_URL}/redfish/v1/Systems/system/Actions/ComputerSystem.Reset"
    data = {"ResetType": "On"}
    response = redfish_session.post(url, json=data, verify=False)
    assert response.status_code == 202  

    time.sleep(5)

    status_response = redfish_session.get(f"{BMC_URL}/redfish/v1/Systems/system", verify=False)
    status_data = status_response.json()
    assert status_data.get("PowerState") == "On"

