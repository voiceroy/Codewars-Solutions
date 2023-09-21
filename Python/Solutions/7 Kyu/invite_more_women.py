def invite_more_women(arr: list) -> bool:
    return not arr.count(1) <= arr.count(-1)
