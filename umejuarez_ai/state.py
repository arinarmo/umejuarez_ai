import collections

from .options import STANCES


def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            r = deep_update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]

    return d


class State(object):
    class __State(object):
        def __init__(self, update_dict):
            self._value = {
                "own": {
                    "stance": STANCES["standing"],
                    "last_action": None,
                    "acting": False,
                    "health": 1
                },
                "enemy": {
                    "health": 1
                },
                "frame": None
            }
            self.update(update_dict)

        def update(self, update_dict):
            self._value = deep_update(self._value, update_dict)


    instance = None
    def __init__(self, update_dict):
        if not State.instance:
            State.instance = State.__State(update_dict)
        else:
            State.instance.update(update_dict)
