import json
import logging
import logging.config

with open("log_config.json") as f:
    log_config = json.load(f)

logging.config.dictConfig(log_config)

logger = logging.getLogger("my_logger")

logger.debug("a = 5")
logger.warning("warning message")

try:
    1 / 0
except ZeroDivisionError:
    # logger.error("zero division", exc_info=True)
    logger.exception("zero division")
