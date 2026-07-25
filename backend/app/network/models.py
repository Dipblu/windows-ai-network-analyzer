from dataclasses import dataclass, field


@dataclass(slots=True)
class NetworkInterface:
    """
    Represents a network interface that WANA can capture packets from.
    """

    name: str
    description: str
    is_up: bool
    mac_address: str | None = None
    ipv4_addresses: list[str] = field(default_factory=list)
    ipv6_addresses: list[str] = field(default_factory=list)
    