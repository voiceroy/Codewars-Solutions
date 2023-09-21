def find_nb(m: int) -> int:
    cubes = 0
    vol = 0
    while True:
        cubes += 1
        vol += cubes**3

        if vol == m:
            return cubes

        if vol > m:
            return -1
