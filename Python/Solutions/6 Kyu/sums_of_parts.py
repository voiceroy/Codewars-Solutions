def parts_sums(ls: list) -> list:
    total = sum(ls)
    result = [total]

    for x in ls:
        total -= x
        result.append(total)

    return result
