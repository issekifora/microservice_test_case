import pytest


@pytest.fixture
def string():
    string = "saippuakivikauppias"
    return string


@pytest.mark.functional
@pytest.mark.usefixtures("client_class")
@pytest.fixture(scope="session")
def test_client():
    from microservice_test_case.app import application as flask_app

    flask_app.debug = True
    flask_app.config["TESTING"] = True
    flask_app.config["SERVER_NAME"] = "localhost"
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture
def api_spec():
    from prance import ResolvingParser

    parser = ResolvingParser(
        "microservice_test_case/app/specs/api.yaml", backend="openapi-spec-validator", strict=False
    )

    return parser.specification
