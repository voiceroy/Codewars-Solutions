def longest_consec(strarr: list, k: int) -> str:
    if strarr:
        if k > len(strarr):
            return ""
        else:
            if k >= 0:
                words = ["".join(strarr[x : x + k]) for x in range(len(strarr))]
            if k < 0:
                words = [
                    "".join(strarr[x : x + abs(k) : k]) for x in range(len(strarr))
                ]
            lengths = [len(x) for x in words]
            return words[lengths.index(max(lengths))]
    else:
        return ""
