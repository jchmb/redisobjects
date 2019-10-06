import unittest
import uuid

from redisobjects.serializers import *

class SerializerTest(unittest.TestCase):
    def assertSerializerConsistent(self, serialized, deserialized, *, serializer=None):
        # Assert that serialized values match expected values.
        self.assertEqual(serialized, list(map(serializer.serialize, deserialized)))
        # Assert that deserialized values match expected values.
        self.assertEqual(deserialized, list(map(serializer.deserialize, serialized)))
        # Assert that x = f^-1(f(x)) for every x.
        self.assertEqual(deserialized, list(map(lambda s: serializer.deserialize(serializer.serialize(s)), deserialized)))

    def test_identity_serializer(self):
        serializer = IdentitySerializer()
        deserialized = [
            b'',
            b'abc',
        ]
        serialized = deserialized
        self.assertSerializerConsistent(serialized, deserialized, serializer=serializer)

    def test_string_serializer(self):
        serializer = StringSerializer()
        deserialized = [
            '',
            'abc',
            'aëöó',
        ]
        serialized = [
            b'',
            b'abc',
            b'a\xc3\xab\xc3\xb6\xc3\xb3',
        ]
        self.assertSerializerConsistent(serialized, deserialized, serializer=serializer)

    def test_json_serializer(self):
        serializer = JsonSerializer(sort_keys=True)
        deserialized = [
            {},
            {'a': '1', 'b': 2},
            {'c': [1, 2, 3]}
        ]
        serialized = [
            '{}',
            '{"a": "1", "b": 2}',
            '{"c": [1, 2, 3]}',
        ]
        self.assertSerializerConsistent(serialized, deserialized, serializer=serializer)

    def test_uuid_serializer(self):
        serializer = UUIDSerializer()
        deserialized = [
            uuid.UUID('ac129a14-38e0-4e77-8c5e-363ba58537f1'),
        ]
        serialized = [
            'ac129a14-38e0-4e77-8c5e-363ba58537f1',
        ]
        self.assertSerializerConsistent(serialized, deserialized, serializer=serializer)

    def test_tuple_serializer(self):
        serializer = TupleSerializer(IdentitySerializer(), StringSerializer(), JsonSerializer(sort_keys=True))
        deserialized = [
            (b'', '', {}),
            (b'abc', 'aëöó', {'a': '1', 'b': 2}),
        ]
        serialized = [
            (b'', b'', '{}'),
            (b'abc', b'a\xc3\xab\xc3\xb6\xc3\xb3', '{"a": "1", "b": 2}'),
        ]
