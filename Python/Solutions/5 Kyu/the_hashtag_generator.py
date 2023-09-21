def generate_hashtag(s: str) -> str | bool:
    s = "".join([s.title() for s in s.split() if s not in " "])
    return f"#{s}" if 0 < len(s) < 139 else False
