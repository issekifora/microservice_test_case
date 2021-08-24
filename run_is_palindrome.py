from microservice_test_case.src.is_palindrome import is_palindrome, EmptyStringError


if __name__ == "__main__":
    import logging
    import logging.config

    import argparse

    logging.config.fileConfig(fname="logging.ini", disable_existing_loggers=False)
    logger = logging.getLogger("CLI")
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--string", help="String to check", required=True, type=str)

    args = parser.parse_args()
    try:
        logger.info(
            "String `{string}` is {answer} palindrome".format(
                string=args.string, answer="a" if is_palindrome(args.string) else "not a"
            )
        )
    except EmptyStringError as e:
        logger.error(e, exc_info=True)
