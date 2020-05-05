from ncclient import manager
import xmltodict
from xml.dom import minidom
from credentials import iosxe


# Import credentials from external file
iosxe_manager = manager.connect(
    host = iosxe["address"],
    port = iosxe["netconf_port"],
    username = iosxe["username"],
    password = iosxe["password"],
    hostkey_verify = False,
    )


print(iosxe_manager.connected)

for capabilitie in iosxe_manager.server_capabilities:
    print(capabilitie)
