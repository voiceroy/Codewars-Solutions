def tribonacci(signature: list, n: int, memo: dict = {}) -> list:
    memo = {x: y for x, y in enumerate(signature)}
    ret_list = []

    for i in range(n):
        if i in memo:
            ret_list.append(memo[i])
        else:
            memo[i] = sum(memo[x] for x in range(i - 3, i))
            ret_list.append(memo[i])

    return ret_list
