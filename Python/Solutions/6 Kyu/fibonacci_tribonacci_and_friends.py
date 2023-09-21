def Xbonacci(signature: list, n: int) -> list:

    return_list = signature[:]

    for i in range(n - len(signature)):
        current_elem = 0

        for elem in return_list[len(return_list) - len(signature) :]:
            current_elem += elem

        return_list.append(current_elem)

    return return_list[:n]
