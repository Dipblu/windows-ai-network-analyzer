import socket

import psutil

from app.network.models import NetworkInterface


def get_network_interfaces() -> list[NetworkInterface]:
    """
    Discover all network interfaces available on the system.
    """

    stats = psutil.net_if_stats()
    addresses = psutil.net_if_addrs()

    interfaces: list[NetworkInterface] = []

    for name, stat in stats.items():

        interface = NetworkInterface(
            name=name,
            description=name,
            is_up=stat.isup,
        )

        # Get all addresses assigned to this interface
        for address in addresses.get(name, []):

            # IPv4
            if address.family == socket.AF_INET:
                interface.ipv4_addresses.append(address.address)

            # IPv6
            elif address.family == socket.AF_INET6:
                interface.ipv6_addresses.append(address.address)

            # MAC Address
            elif str(address.family) == "-1":
                interface.mac_address = address.address

        interfaces.append(interface)

    return interfaces