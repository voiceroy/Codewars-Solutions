def sort_array(source_array: list) -> list:
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]
