def rev_rot(string: str, sz: int) -> str:
    if len(string) > sz > 0:
        string_chunks = [
            string[i : i + sz] for i in range(0, len(string) - (len(string) % sz), sz)
        ]

        return_string = ""

        for chunk in string_chunks:
            if sum(int(x) ** 3 for x in chunk) % 2 == 0:
                return_string += chunk[::-1]
            else:
                return_string += chunk[1:] + chunk[0]

        return return_string
    else:
        return ""
