def make_readable(seconds: int) -> str:
    hour = seconds // 3600
    minutes = (seconds // 60) - (hour * 60)
    seconds = seconds - ((minutes * 60) + (hour * 3600))
    return f"{hour:02}:{minutes:02}:{seconds:02}"
