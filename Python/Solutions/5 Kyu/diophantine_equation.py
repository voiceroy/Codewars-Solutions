from math import sqrt


def sol_equa(n: int) -> list:
    solutions = []

    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            y = n // x

            if (x + y) % 2 == 0 and (y - x) % 4 == 0:
                x_sol = (x + y) // 2
                y_sol = (y - x) // 4

                solutions.append([x_sol, y_sol])

    return solutions
