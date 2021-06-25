import logging as log


def returns_logger():
    """
    creates an custom logger
    :return: returns already created custom logger
    """
    custom_log = log.getLogger("another")
    custom_handler = log.FileHandler('address_book_log.log', mode='w')
    custom_handler.setLevel(log.DEBUG)
    custom_formatter = log.Formatter('%(message)s - %(lineno)d - %(pathname)s')
    custom_handler.setFormatter(custom_formatter)
    custom_log.addHandler(custom_handler)
    return custom_log
