import json
from decimal import Decimal
from datetime import date, datetime


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode()
        return json.JSONEncoder.default(self, obj)


def json_dumps(data=None):
    return json.dumps(data, cls=JSONEncoder)
