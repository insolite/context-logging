import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from context_logging.advanced_json_encoder import AdvancedJsonEncoder


LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(message)-20s %(context)s'


class JsonSerializableObject(MagicMock):

    def __init__(self, represent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.represent = represent

    def __json__(self):
        return self.represent


class NotStrObject:

    def __str__(self):
        raise Exception


class AdvancedJsonEncoderTest(TestCase):

    def setUp(self):
        super().setUp()
        self.encoder = AdvancedJsonEncoder()

    def test_default__json_magic(self):
        expected_represent = MagicMock()
        obj = JsonSerializableObject(expected_represent)

        represent = self.encoder.default(obj)

        self.assertEqual(represent, expected_represent)

    def test_default__datetime(self):
        obj = datetime.datetime.utcnow()

        represent = self.encoder.default(obj)

        self.assertEqual(represent, str(obj))

    def test_default__timedelta(self):
        obj = datetime.timedelta(hours=1, minutes=2)

        represent = self.encoder.default(obj)

        self.assertEqual(represent, str(obj))

    def test_default__bytes(self):
        obj = bytes(b'foo')

        represent = self.encoder.default(obj)

        self.assertEqual(represent, str(obj))

    def test_default__default(self):
        obj = 'foo'

        represent = self.encoder.default(obj)

        self.assertEqual(represent, obj)

    def test_default__type_error(self):
        obj = NotStrObject()

        self.assertRaises(TypeError, self.encoder.default, obj)