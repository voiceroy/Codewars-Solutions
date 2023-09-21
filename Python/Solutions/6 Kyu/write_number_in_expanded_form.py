def expanded_form(num: int) -> str:
    places = [[i, x] for i, x in enumerate(str(num)[::-1]) if int(x) > 0]
    return " + ".join([f"{10**num[0]*int(num[1])}" for num in places[::-1]]).strip()
