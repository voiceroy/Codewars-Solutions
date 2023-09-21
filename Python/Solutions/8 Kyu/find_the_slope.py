def find_slope(points: list) -> int | str:
    if points[0] - points[2] != 0:
        slope = (points[1] - points[3]) / (points[0] - points[2])
        if slope == int(slope):
            return str(int(slope))
        else:
            return "undefined"
    else:
        return "undefined"
