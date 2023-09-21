def is_int_array(arr: list) -> bool:
    if type(arr) == list:
        if arr:
            for x in arr:
                try:
                    if int(x) != x:
                        return False
                except (ValueError, TypeError):
                    return False
            else:
                return True
        else:
            return True
    else:
        return False
