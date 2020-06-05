def dunder_it(x: str) -> (str, Exception):
    try:
        return f"__{str(x).lstrip('_').rstrip('_')}__"
    except Exception as e:
        return ""  # skip errors
        # return e
