import logging
import json


EXTRA_KEY = 'extra'


class ContextLoggerAdapter(logging.LoggerAdapter):

    def __init__(self, logger, json_encoder_class, extra):
        super().__init__(logger, extra)
        self.json_encoder_class = json_encoder_class

    def process(self, msg, kwargs):
        extra_args = kwargs.copy()
        actual_args = {}
        for key in (EXTRA_KEY, 'exc_info', 'stack_info'):
            if key in kwargs:
                actual_args[key] = extra_args.pop(key)
        if EXTRA_KEY in actual_args:
            extra_args.update(actual_args[EXTRA_KEY])
        else:
            actual_args[EXTRA_KEY] = {}
        context_str = ', '.join(['{}={}'.format(key, json.dumps(val, cls=self.json_encoder_class))
                                 for extra in (self.extra, extra_args)
                                 for key, val in sorted(extra.items(),
                                                        key=lambda x: x[0])])
        actual_args[EXTRA_KEY]['context'] = context_str
        return msg, actual_args
