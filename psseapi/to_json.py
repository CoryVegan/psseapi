import json

class ComplexEncoder(json.JSONEncoder):
    """JSONEncoder to handle complex values
    usage:
        `json.dumps(d, cls=ComplexEncoder, indent=4)`
    """
    def default(self, obj):
        if isinstance(obj, complex):
            return str(obj).replace("(", "").replace(")", "")
        # else return default implementation
        return json.JSONEncoder.default(self, obj)

