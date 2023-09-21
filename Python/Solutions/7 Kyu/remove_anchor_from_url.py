def remove_url_anchor(url: str) -> str:
    try:
        return url[: url.index("#")]
    except ValueError:
        return url
