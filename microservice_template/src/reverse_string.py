import logging.config


logger = logging.getLogger(__name__)


class EmptyStringError(Exception):
    pass


def reverse_string(string):
    """
    Reversed a string provided. Cannot reverse empty string.
    :param string: String to reverse
    :return: Reversed string
    """
    if not len(string):
        raise EmptyStringError("Empty strings are not supported yet!")

    logger.debug(string)

    string_reversed = string[::-1]

    logger.debug(string_reversed)

    return string_reversed
