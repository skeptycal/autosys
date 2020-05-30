import autosys


def json_prettyprint():
    """Pretty-print information as JSON."""
    print(json.dumps(info(), sort_keys=True, indent=2))
