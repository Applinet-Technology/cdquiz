def pretty_time(seconds):
    if seconds is None:
        return "0s"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    parts = []
    if h: parts.append(f"{h}h")
    if m: parts.append(f"{m}m")
    parts.append(f"{s}s")
    return " ".join(parts)




def format_duration(seconds):

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"

    if minutes > 0:
        return f"{minutes}m {secs}s"

    return f"{secs}s"