import datetime
from json.encoder import JSONEncoder


class AdvancedJsonEncoder(JSONEncoder):

    def default(self, o):
        if hasattr(o, '__json__'):
            return o.__json__()
        elif isinstance(o, datetime.datetime):
            return str(o)
        elif isinstance(o, datetime.timedelta):
            return str(o)
        elif isinstance(o, bytes):
            return str(o)
        try:
            return str(o)
        except Exception:
            return super().default(o)
