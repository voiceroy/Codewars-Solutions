def create_phone_number(n: list) -> str:
    n = [str(x) for x in n]
    return f'({"".join(n[0:3])}) {"".join(n[3:6])}-{"".join(n[6:10])}'
