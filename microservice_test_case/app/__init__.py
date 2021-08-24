import logging.config

import connexion
from flask.logging import create_logger
import pathlib


logging_ini = str(pathlib.Path(*[i for i in pathlib.Path.cwd().parts if i != "tests"]).joinpath("logging.ini"))


logging.config.fileConfig(fname=logging_ini, disable_existing_loggers=False)
logging.getLogger("connexion").setLevel(logging.WARNING)
logging.getLogger("openapi_spec_validator").setLevel(logging.WARNING)


app = connexion.App(__name__, specification_dir="./specs")
app.add_api("api.yaml", strict_validation=True, validate_responses=True)


application = app.app
logger = create_logger(application)
logger.info("Started")
