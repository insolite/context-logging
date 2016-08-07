import logging
from unittest import TestCase
from unittest.mock import MagicMock

from formatters import ColoredFormatter


LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(message)-20s %(context)s'


class ContextFormatterTest(TestCase):

    def setUp(self):
        super().setUp()
        self.formatter = ColoredFormatter()
        self.record = MagicMock()

    def test_format(self):
        self.record.levelno = logging.WARNING

        self.formatter.format(self.record)