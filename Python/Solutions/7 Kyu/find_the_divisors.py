def divisors(integer: int) -> list | str:
    divisors_list = [x for x in range(2, integer) if integer % x == 0]
    return divisors_list if len(divisors_list) > 0 else f"{integer} is prime"
