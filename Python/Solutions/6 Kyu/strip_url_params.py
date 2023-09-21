def strip_url_params(url: str, params_to_strip: list = []) -> str:
    split = url.split("?")

    if len(split) == 1 or split[1] == "":
        return split[0]

    parameters = {}

    for params in split[1].split("&"):
        var, val = params.split("=")

        if var in params_to_strip:
            continue

        if var not in parameters:
            parameters[var] = val

    if parameters:
        param_string = "&".join(f"{x}={y}" for x, y in parameters.items())
    else:
        param_string = ""

    return f"{split[0]}?" + param_string if param_string else split[0]
