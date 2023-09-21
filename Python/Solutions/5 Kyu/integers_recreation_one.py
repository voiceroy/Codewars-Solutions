from math import sqrt


def list_squared(m: int, n: int) -> list:
    squared_list = []

    for num in range(m, n + 1):
        factors = set()

        for i in range(1, int(sqrt(num) + 1)):
            if num % i == 0:
                factors.add(i**2)
                factors.add(int(num / i) ** 2)

        factor_square_sum = sum(factors)

        if sqrt(factor_square_sum).is_integer():
            squared_list.append([num, factor_square_sum])

    return squared_list
