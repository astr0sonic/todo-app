import logging


class MyFormatter(logging.Formatter):
    def format(self, log_record: logging.LogRecord) -> str:
        return f"{log_record.name} - {log_record.levelname} - {log_record.msg}"
