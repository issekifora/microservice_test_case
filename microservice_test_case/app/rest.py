from microservice_test_case.src.is_palindrome import is_palindrome, EmptyStringError


def get_reversed_string(body):
    result = {}

    string = body["params"]["string"]

    try:
        result["result"] = {"string": string, "is_palindrome": is_palindrome(string)}
        return result, 201
    except EmptyStringError as error:
        result["error"] = {"code": 1010, "message": str(error)}
        return result, 201
    except Exception as error:
        result["error"] = {"code": 1000, "message": str(error)}
        return result, 201
