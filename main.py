import requests
from requests.auth import HTTPBasicAuth
import json

# Replace these variables with your own ISE instance details
ISE_HOST = 'https://devnetsandboxise.cisco.com'
USERNAME = 'readonly'
PASSWORD = 'ISEisC00L'
ISE_API_ENDPOINT = '/ers/config/networkdevice'
NAD_LIST = []
# Disable warnings for unverified HTTPS requests
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_network_devices(host, username, password):
    NAD_LIST = []
    url = f"{host}{ISE_API_ENDPOINT}"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve network devices. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

#get the device details for each NAD
def get_nad_details(nad_url, username, password):
    url = f"{nad_url}"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve NAD. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

if __name__ == "__main__":
    devices = get_network_devices(ISE_HOST, USERNAME, PASSWORD)
    if devices:
        for resource in devices["SearchResult"]["resources"]:
            device_direct_link = resource["link"]["href"]
            NAD_LIST.append(device_direct_link)
        for nad in NAD_LIST:
            idk = get_nad_details(nad, USERNAME, PASSWORD)
            print(idk)
