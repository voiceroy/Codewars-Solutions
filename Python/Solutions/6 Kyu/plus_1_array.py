def up_array(arr: list) -> list | None:
    return (
        [
            int(x)
            for x in str(int("".join(str(x) for x in arr)) + 1).rjust(len(arr), "0")
        ]
        if len(arr) > 0 and all(9 >= x >= 0 for x in arr)
        else None
    )
