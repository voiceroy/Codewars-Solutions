def is_valid_coordinates(coordinates: str) -> bool:
    try:
        lat, long = (abs(float(x)) for x in coordinates.split(", ") if "e" not in x)
    except ValueError:
        return False

    return lat <= 90 and long <= 180
