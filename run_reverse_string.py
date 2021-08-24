from microservice_template.src.reverse_string import reverse_string, EmptyStringError


if __name__ == "__main__":
    import logging
    import logging.config

    import argparse

    logging.config.fileConfig(fname="logging.ini", disable_existing_loggers=False)
    logger = logging.getLogger('CLI')

    parser = argparse.ArgumentParser()
    parser.add_argument("--string", help="String to reverse", required=True, type=str)

    args = parser.parse_args()
    try:
        reversed_string = reverse_string(args.string)
    except EmptyStringError as e:
        logger.error(e, exc_info=True)
