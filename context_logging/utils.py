import logging

from .context_logger_adapter import ContextLoggerAdapter
from .advanced_json_encoder import AdvancedJsonEncoder


def uncaught_exception(exctype, value, tb):
    logger = getLogger()
    try:
        raise value
    except:
        logger.critical('uncaught_exception', name=exctype.__name__, exc_info=True)


def getLogger(name=None, **kwargs):
    return ContextLoggerAdapter(logging.getLogger(name), AdvancedJsonEncoder, kwargs)