def get_length_of_missing_array(array_of_arrays: list) -> int:
    if array_of_arrays is None or len(array_of_arrays) == 0:
        return 0

    lengths = {}

    for array in array_of_arrays:
        if array is None:
            return 0
        elif len(array) == 0:
            return 0

        lengths[len(array)] = array

    return list(
        set(range(min(lengths.keys()), max(lengths.keys()) + 1)).difference(
            lengths.keys()
        )
    )[0]
