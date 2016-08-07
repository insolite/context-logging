from json.encoder import JSONEncoder
from unittest import TestCase
from unittest.mock import MagicMock

from context_logger_adapter import ContextLoggerAdapter, EXTRA_KEY


class ContextLoggerAdapterTest(TestCase):

    def setUp(self):
        super().setUp()
        self.logger = MagicMock()
        self.json_encode_class = JSONEncoder
        self.extra = {'foo': 'bar'}
        self.logger_adapter = ContextLoggerAdapter(self.logger, self.json_encode_class, self.extra)

    def test_process__exc_info(self):
        src_msg = 'foo'
        src_kwargs = {'test': 42, 'exc_info': True}

        msg, args = self.logger_adapter.process(src_msg, src_kwargs)

        self.assertEqual(msg, src_msg)
        self.assertEqual(args, {'exc_info': True, EXTRA_KEY: {'context': 'foo="bar", test=42'}})

    def test_process__extra(self):
        src_msg = 'foo'
        src_kwargs = {'test': 42, 'extra': {'test2': 24}}

        msg, args = self.logger_adapter.process(src_msg, src_kwargs)

        self.assertEqual(msg, src_msg)
        self.assertEqual(args, {EXTRA_KEY: {'context': 'foo="bar", test=42, test2=24', 'test2': 24}})