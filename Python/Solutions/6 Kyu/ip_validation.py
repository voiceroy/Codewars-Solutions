import ipaddress


def is_valid_IP(string: str) -> bool:
    try:
        return bool(ipaddress.ip_address(string))
    except ValueError:
        return False
