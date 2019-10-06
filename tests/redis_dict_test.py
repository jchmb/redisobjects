import unittest

from redisobjects import connect_fakeredis
from .async_test import async_test

class RedisDictTest(unittest.TestCase):
    @async_test
    async def test_new_dict_is_empty(self):
        redis = connect_fakeredis()
        test_dict = redis.dict('test:dict')
        self.assertEqual(0, await test_dict.size())

    @async_test
    async def test_for_every_element_added_dict_size_increases_by_one(self):
        redis = connect_fakeredis()
        test_dict = redis.dict('test:dict')
        n = 5
        for i in range(n):
            self.assertEqual(i, await test_dict.size())
            await test_dict.set('key_%s' % (i,), 'value_%s' % (i,))
        self.assertEqual(n, await test_dict.size())

    @async_test
    async def test_set_dict_element_is_later_returned_by_get(self):
        redis = connect_fakeredis()
        test_dict = redis.dict('test:dict')
        n = 5
        for i in range(n):
            key = ('key_%s' % (i,)).encode()
            value = ('value_%s' % (i,)).encode()
            self.assertIsNone(await test_dict.get(key))
            await test_dict.set(key, value)
            self.assertEqual(value, await test_dict.get(key))

    @async_test
    async def test_remove_element_from_dict_then_get_returns_none(self):
        redis = connect_fakeredis()
        test_dict = redis.dict('test:dict')
        await test_dict.set('key', 'value')
        await test_dict.remove('key')
        self.assertIsNone(await test_dict.get('key'))
