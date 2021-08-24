from microservice_template.src.reverse_string import reverse_string, EmptyStringError


def get_reversed_string(body):
    result = {}

    string = body["params"]["string"]

    try:
        result["result"] = {"string": reverse_string(string)}
        return result, 201
    except EmptyStringError as error:
        result["error"] = {"code": 1010, "message": str(error)}
        return result, 201
    except Exception as error:
        result["error"] = {"code": 1000, "message": str(error)}
        return result, 201
