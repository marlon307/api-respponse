def unique(list: list[dict]):
    return [dict(t) for t in {tuple(d.items()) for d in list}]
