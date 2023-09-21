def snail(snail_map: list) -> list:
    results = []
    while len(snail_map) > 0:

        # Move right
        results += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            # Go down
            for i in snail_map:
                results += [i[-1]]
                del i[-1]

            # Move left
            if snail_map[-1]:
                results += snail_map[-1][::-1]
                del snail_map[-1]

            # Go up
            for i in reversed(snail_map):
                results += [i[0]]
                del i[0]

    return results
