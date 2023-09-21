def format_duration(seconds: int) -> str:
    if not seconds:
        return "now"

    time_units = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1,
    }
    converted = []

    for time_unit in time_units:
        in_time_unit, seconds = divmod(seconds, time_units[time_unit])

        if in_time_unit < 1:
            continue
        elif in_time_unit > 1:
            converted.append(f"{in_time_unit} {time_unit}s")
        else:
            converted.append(f"{in_time_unit} {time_unit}")

    return (
        ", ".join(converted[:-1]) + " and " + converted[-1]
        if len(converted) > 1
        else converted[0]
    )
