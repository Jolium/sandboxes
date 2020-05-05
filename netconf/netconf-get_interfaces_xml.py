from ncclient import manager
import xmltodict
from xml.dom import minidom

# import credentials
from credentials import iosxe


# credentials from external file

iosxe_manager = manager.connect(
    host = iosxe["address"],
    port = iosxe["netconf_port"],
    username = iosxe["username"],
    password = iosxe["password"],
    hostkey_verify = False,
    )


print(iosxe_manager.connected)


# create filter for interfaces
filter_interfaces = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
    </interface>
  </interfaces>
</filter>
"""

# print response ok
iosxe_interfaces = iosxe_manager.get_config("running", filter_interfaces)
print(iosxe_interfaces.ok)

# print interfaces in xml format
iosxe_config_xml = minidom.parseString(iosxe_interfaces.xml)
print(iosxe_config_xml.toprettyxml(indent= "  "))


"""
iosxe_gig2_dict = xmltodict.parse(iosxe_GigabitEthernet2.xml)
intf = iosxe_gig2_dict["rpc-reply"]["data"]
print(intf)
print()
print(intf.keys())
print()
print(intf["interfaces"]["interface"]["name"])
print(intf["interfaces"]["interface"]["description"])
print(intf["interfaces"]["interface"]["enabled"])
"""
