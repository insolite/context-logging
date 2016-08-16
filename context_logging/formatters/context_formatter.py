import logging


class ContextFormatter(logging.Formatter):

    def format(self, record):
        if not hasattr(record, 'context'):
            record.context = ''
        return super().format(record)
