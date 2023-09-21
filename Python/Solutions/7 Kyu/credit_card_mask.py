def maskify(cc: str) -> str:
    return len(cc[:-4]) * "#" + cc[::-1][:4][::-1] if len(cc) > 4 else cc
