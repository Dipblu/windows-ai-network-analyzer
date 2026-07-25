import ipaddress

from app.network.interfaces import get_network_interfaces
from app.network.models import NetworkInterface


def test_get_network_interfaces():
    interfaces = get_network_interfaces()

    # The function should return a non-empty list.
    assert isinstance(interfaces, list)
    assert len(interfaces) > 0

    for interface in interfaces:

        # Every item should be a NetworkInterface object.
        assert isinstance(interface, NetworkInterface)

        # Every interface should have a name.
        assert interface.name.strip() != ""

        # is_up should always be a boolean.
        assert isinstance(interface.is_up, bool)

        # Validate IPv4 addresses.
        for address in interface.ipv4_addresses:
            ipaddress.IPv4Address(address)

        # Validate IPv6 addresses.
        for address in interface.ipv6_addresses:
            ipaddress.IPv6Address(address)

        print(interface)