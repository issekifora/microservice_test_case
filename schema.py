import fastjsonschema

REQUEST_APP = {"string": {"type": "string"}}
RESPONSE_APP = {"string": {"type": "string"}}

REQUEST_JSON_RPC = {
    "type": "object",
    "description": "Request compatible with  JSON RPC 2.0 specification",
    "oneOf": [
        {"description": "An individual request", "$ref": "#/definitions/request"},
        {"description": "An array of requests", "type": "array", "items": {"$ref": "#/definitions/request"}},
    ],
    "definitions": {
        "request": {
            "type": "object",
            "additionalProperties": True,
            "required": ["jsonrpc", "method"],
            "properties": {
                "jsonrpc": {"enum": ["2.0"]},
                "method": {"type": "string"},
                "id": {"type": ["string", "null"],},
                "params": {"type": "object", "properties": REQUEST_APP,},
            },
        }
    },
}


RESPONSE_JSON_RPC = {
    "type": "object",
    "description": "A JSON RPC 2.0 response",
    "oneOf": [
        {"$ref": "#/definitions/success"},
        {"$ref": "#/definitions/error"},
        {"type": "array", "items": {"oneOf": [{"$ref": "#/definitions/success"}, {"$ref": "#/definitions/error"}]}},
    ],
    "definitions": {
        "common": {
            "required": ["id", "jsonrpc"],
            "not": {"description": "cannot have result and error at the same time", "required": ["result", "error"]},
            "type": "object",
            "properties": {"id": {"type": ["string", "null"],}, "jsonrpc": {"enum": ["2.0"]}},
        },
        "success": {
            "description": "A success. The result member is then required and can be anything.",
            "allOf": [{"$ref": "#/definitions/common"}, {"required": ["result"]}],
            "properties": {"result": {"type": "object", "properties": RESPONSE_APP},},
        },
        "error": {
            "allOf": [
                {"$ref": "#/definitions/common"},
                {
                    "required": ["error"],
                    "properties": {
                        "error": {
                            "type": "object",
                            "required": ["code", "message"],
                            "properties": {
                                "code": {"type": "integer"},
                                "message": {"type": "string"},
                                "data": {"description": "optional, can be anything"},
                            },
                        }
                    },
                },
            ]
        },
    },
}

validator_request = fastjsonschema.compile(REQUEST_JSON_RPC)
validator_response = fastjsonschema.compile(RESPONSE_JSON_RPC)
