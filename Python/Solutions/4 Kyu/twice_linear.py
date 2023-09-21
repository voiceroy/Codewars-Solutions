from collections import deque


def dbl_linear(n: int) -> int:
    x = 1
    cnt = 0
    y, z = deque([]), deque([])

    while True:
        if cnt == n:
            return x

        y.append(2 * x + 1)
        z.append(3 * x + 1)

        x = min(y[0], z[0])

        if x == y[0]:
            x = y.popleft()
        if x == z[0]:
            x = z.popleft()

        cnt += 1
