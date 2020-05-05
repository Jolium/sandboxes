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

##
## Show created Loopback
##

filter_loopback = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1024</name>
    </interface>
  </interfaces>
</filter>
"""

iosxe_loopback = iosxe_manager.get_config("running", filter_loopback)
print(iosxe_loopback.ok)

iosxe_config_xml = minidom.parseString(iosxe_loopback.xml)
print(iosxe_config_xml.toprettyxml(indent= "  "))

##
## Delete created Loopback
##

delete_loopback = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface operation="delete">
      <name>Loopback1024</name>
    </interface>
  </interfaces>
</config>
"""

iosxe_delete_loopback = iosxe_manager.edit_config(target = "running", config = delete_loopback)
print(iosxe_delete_loopback.ok)

##
## Show deleted Loopback
##

filter_loopback = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1024</name>
    </interface>
  </interfaces>
</filter>
"""

iosxe_loopback = iosxe_manager.get_config("running", filter_loopback)
print(iosxe_loopback.ok)

iosxe_config_xml = minidom.parseString(iosxe_loopback.xml)
print(iosxe_config_xml.toprettyxml(indent= "  "))
