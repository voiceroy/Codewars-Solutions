def camel_case(string: str) -> str:
    return "".join(x.title() for x in string.split(" "))
