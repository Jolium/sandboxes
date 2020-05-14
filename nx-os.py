#!/usr/bin/env python3

import requests
import json


# Disables ssl warnings when a request is made to an
# HTTPS URL without certificate verification enabled
requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning
 )

"""
Modify these please
"""
url = "https://sbx-nxos-mgmt.cisco.com/ins"
switchuser = "admin"
switchpassword = "Admin_1234!"

myheaders = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show hostname ; show version",
        "output_format": "json",
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheaders,
    auth=(switchuser, switchpassword),
    verify=False,
).json()

print(json.dumps(response, indent=2))
