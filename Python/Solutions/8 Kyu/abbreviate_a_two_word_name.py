def abbrev_name(name: str) -> str:
    return ".".join([x[0].upper() for x in name.split()])
