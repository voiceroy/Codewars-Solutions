def wave(people: str) -> list:
    people = list(people)
    ret = []

    for i in range(len(people)):
        if not people[i] in " ":
            people_c = people[:]
            people_c[i] = people[i].upper()
            ret.append("".join(people_c))
        else:
            continue

    return ret
