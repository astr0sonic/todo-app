import logging
import sys

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("my_logger")
# logger2 = logging.getLogger("my_logger.my")
# logger2.propagate = True
# logger2.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="[%(asctime)s] %(levelname)s %(name)s %(lineno)d - [%(message)s]"
)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="logs.log")
file_handler.setLevel(logging.WARNING)

logger.addHandler(handler)
logger.addHandler(file_handler)

logger.debug("a = 5")
logger.warning("warning message")

try:
    1 / 0
except ZeroDivisionError:
    # logger.error("zero division", exc_info=True)
    logger.exception("zero division")


# formatter - как печатать?
# handler - где/куда печать?
# filter - фильтрует сообщения

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("this is debug message")
# logging.info("this is info message")
# logging.warning("this is debug message")
# logging.error("this is error message")
# logging.critical("this is critical message")
