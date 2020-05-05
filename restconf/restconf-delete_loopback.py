# import the requests library
import requests
import sys

# import credentials
from credentials import iosxe 

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# credentials from external file
host = iosxe["address"]
port = iosxe["restconf_port"]
username = iosxe["username"]
password = iosxe["password"]

# delete loopback
loopback = "Loopback112"

# create a main() method
def main():
    """Main method that configures the Ip address for a interface via RESTCONF."""

    # url string to issue GET request
    url = f"https://{host}:{port}/restconf/data/ietf-interfaces:interfaces/interface={loopback}"
    

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    
    # this statement performs a DELETE on the specified url
    response = requests.request("DELETE",url, auth=(username, password), headers=headers, verify=False)   
    
    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    sys.exit(main())
