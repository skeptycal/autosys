# 'package imports'
# 'Standard Library'
import json


def json_prettyprint(obj: object):
    """Pretty-print information as JSON."""
    print(json.dumps(obj, sort_keys=True, indent=2))
