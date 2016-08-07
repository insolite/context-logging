import logging

from formatters.context_formatter import ContextFormatter


COLOR_FORMAT = '\x1B[{}'

COLOR_RESET = '0m'
COLOR_WHITE = '01;1m'
COLOR_RED = '01;31m'
COLOR_YELLOW = '01;33m'
COLOR_BRGREEN = '01;32m'
COLOR_MAGENTA = '01;35m'


color_map = ((logging.CRITICAL, COLOR_MAGENTA),
             (logging.ERROR, COLOR_RED),
             (logging.WARNING, COLOR_YELLOW),
             (logging.INFO, COLOR_WHITE),
             (logging.DEBUG, COLOR_BRGREEN))


class ColoredFormatter(ContextFormatter):

    def format(self, record):
        message = super().format(record)
        color = COLOR_RESET
        for level, clr in color_map:
            if record.levelno >= level:
                color = clr
                break
        return COLOR_FORMAT.format(color) + message + COLOR_FORMAT.format(COLOR_RESET)