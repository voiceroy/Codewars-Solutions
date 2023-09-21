from ipaddress import IPv4Address


def ips_between(start: str, end: str) -> int:
    return int(IPv4Address(end)) - int(IPv4Address(start))
