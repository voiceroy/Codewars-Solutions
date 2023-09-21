def interpret_as_int32(stream: list) -> list:
    bytes_list = b"".join(stream)

    return [
        int.from_bytes(bytes_list[x : x + 4], "big", signed=True)
        for x in range(0, (len(bytes_list) // 4) * 4, 4)
    ]
