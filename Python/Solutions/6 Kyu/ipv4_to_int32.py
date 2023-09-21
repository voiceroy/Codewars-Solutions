from ipaddress import IPv4Address


def ip_to_int32(ip: str) -> int:
    return IPv4Address(ip)._ip_int_from_string(ip)
