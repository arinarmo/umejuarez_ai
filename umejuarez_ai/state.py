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

    def get_stance(self):
        own = self.instance._value["own"]
        if "stance" in own:
            return own["stance"]
        else:
            return None

    def get_action(self):
        own = self.instance._value["own"]
        if "action" in own:
            return own["stance"]
        else:
            return None

    def acting(self):
        own = self.instance._value["own"]
        return "acting" in own and own["acting"]

    def get_own_health(self):
        own = self.instance._value["own"]
        return own["health"]

    def get_enemy_health(self):
        enemy = self.instance.value["enemy"]
        return enemy["health"]
