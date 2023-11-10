# Use the DNA Center API documentation to help you fix this authentication code snippet https://developer.cisco.com/docs/dna-center/#!authentication-api
# Once fixed you should see a token printed to the console.

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/authenticationAPI/token"

payload = {}
headers = {
    'Authorization': 'Standard ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
    }

response = requests.request('method', url, headers=headers, data = payload, verify=False)
print(response.text)

