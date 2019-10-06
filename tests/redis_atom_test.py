import unittest
import asyncio

from redisobjects import connect_fakeredis
from .async_test import async_test

class RedisAtomTest(unittest.TestCase):
    def _create_connection(self):
        return connect_fakeredis()

    @async_test
    async def test_new_atom_is_empty(self):
        redis = self._create_connection()
        atom = redis.atom('test:atom')
        value = await atom.get()
        # Newly created atom with fresh db must be None.
        self.assertIsNone(value)

    @async_test
    async def test_atom_set_is_returned_by_atom_get(self):
        redis = self._create_connection()
        atom = redis.atom('test:atom')
        value = b'test_value'
        await atom.set(value)
        self.assertEqual(value, await atom.get())

    @async_test
    async def test_atom_set_then_delete_atom_get_returns_none(self):
        redis = self._create_connection()
        atom = redis.atom('test:atom')
        value = b'test_value'
        await atom.set(value)
        await atom.delete()
        self.assertIsNone(await atom.get())
