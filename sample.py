import sys
import logging.config

from context_logging import getLogger, uncaught_exception # context_logging


LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(message)-20s %(context)s'


class Example():

    def __init__(self, context):
        self.context = context
        self.logger = getLogger(__name__, context=self.context)

    def calc(self, src_value):
        self.logger.info('calc', src_value=src_value)
        return src_value + 1

    def execute(self, src_value):
        self.logger.info('execute_start')
        dst_value = self.calc(src_value)
        self.logger.info('result', dst_value=dst_value)
        self.logger.warning('different_items', foo=1, bar='test', test_list=[42], dict={'foo': 'bar'})


def init_logging():
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'standard': {
                'format': LOGGING_FORMAT,
            },
            'colored': {
                '()': 'context_logging.ColoredFormatter',
                'format': LOGGING_FORMAT,
            },
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
            },
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    })
    sys.excepthook = uncaught_exception


def main():
    init_logging()
    example = Example('executor')
    example.execute(42)


if __name__ == '__main__':
    main()