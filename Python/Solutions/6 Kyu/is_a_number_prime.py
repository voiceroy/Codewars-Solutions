def is_prime(num: int) -> bool:
    if num > 1:
        for x in range(2, int(num ** (1 / 2)) + 1):
            if num % x == 0:
                return False
        else:
            return True
    else:
        return False
