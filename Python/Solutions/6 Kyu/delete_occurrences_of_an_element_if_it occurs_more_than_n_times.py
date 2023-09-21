def delete_nth(order: list, max_e: int) -> list:
    lst = list()
    for x in order:
        if lst.count(x) < max_e:
            lst.append(x)
    return lst
