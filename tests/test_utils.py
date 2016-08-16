from unittest import TestCase
from unittest.mock import MagicMock, patch

from context_logging import utils


LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(message)-20s %(context)s'


class UtilsTest(TestCase):

    def test_uncaught_exception(self):
        logger = MagicMock()
        excection_class = Exception

        with patch.object(utils, 'getLogger', MagicMock(return_value=logger)) as getLoggerMock:
            utils.uncaught_exception(excection_class, excection_class(), MagicMock())

        getLoggerMock.assert_called_once_with()
        logger.critical.assert_called_once_with('uncaught_exception', name=excection_class.__name__, exc_info=True)

    def test_getLogger(self):
        logger = MagicMock()
        logger_adapter = MagicMock()
        name = MagicMock()
        kwargs = {'foo': 'bar'}

        with patch.object(utils, 'ContextLoggerAdapter', MagicMock(return_value=logger_adapter)) as ContextLoggerAdapterMock,\
             patch.object(utils.logging, 'getLogger', MagicMock(return_value=logger)) as getLoggerMock,\
             patch.object(utils, 'AdvancedJsonEncoder') as AdvancedJsonEncoderMock:
            wrapped_logger = utils.getLogger(name, **kwargs)

        getLoggerMock.assert_called_once_with(name)
        ContextLoggerAdapterMock.assert_called_once_with(logger, AdvancedJsonEncoderMock, kwargs)
        self.assertEqual(wrapped_logger, logger_adapter)