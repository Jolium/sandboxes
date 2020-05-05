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
## Create Loopback
##

create_loopback = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1024</name>
      <description>My new Loopback</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
        ianaift:softwareLoopback
      </type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>172.31.231.231</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""

iosxe_create_loopback = iosxe_manager.edit_config(target = "running", config = create_loopback)
print(iosxe_create_loopback.ok)

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

