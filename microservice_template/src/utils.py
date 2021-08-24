def prepare_response_success(string, _id=None):
    return {"jsonrpc": "2.0", "result": {"string": string}, "id": _id}


def prepare_response_error(code, message, _id=None):
    return {"jsonrpc": "2.0", "error": {"code": code, "message": message}, "id": _id}


def prepare_request(string, method="reverse_string", _id=None):
    return {"jsonrpc": "2.0", "params": {"string": string}, "id": _id, "method": method}
