import re


def domain_name(url: str) -> str:
    exp = re.compile(r"(^(http|https):\/\/)?(www.)?(?P<Domain>[\w\S][^./]*)")
    match = exp.search(url)
    return match.group("Domain")
