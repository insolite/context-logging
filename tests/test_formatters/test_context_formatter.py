from unittest import TestCase
from unittest.mock import MagicMock

from formatters import ContextFormatter


LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(message)-20s %(context)s'


class ContextFormatterTest(TestCase):

    def setUp(self):
        super().setUp()
        self.formatter = ContextFormatter()
        self.record = MagicMock()

    def test_format__context_defined(self):
        context = MagicMock()
        self.record.context = context

        self.formatter.format(self.record)

        self.assertEqual(self.record.context, context)

    def test_format__context_not_defined(self):
        del self.record.context

        self.formatter.format(self.record)

        self.assertEqual(self.record.context, '')