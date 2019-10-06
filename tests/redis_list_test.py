import unittest
import asyncio

from redisobjects import connect_fakeredis

def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
    return wrapper

class RedisListTest(unittest.TestCase):
    def _create_connection(self):
        return connect_fakeredis()

    @async_test
    async def test_new_list_is_empty(self):
        redis = self._create_connection()
        test_list = redis.list('test:list')
        self.assertEqual(0, await test_list.size())

    @async_test
    async def test_for_every_element_right_pushed_list_size_grows_by_one(self):
        redis = self._create_connection()
        test_list = redis.list('test:list')
        n = 5
        for i in range(n):
            self.assertEqual(i, await test_list.size())
            await test_list.push_right('dummy_value_%s' % (i,))
        self.assertEqual(n, await test_list.size())

    @async_test
    async def test_for_every_element_left_pushed_list_size_grows_by_one(self):
        redis = self._create_connection()
        test_list = redis.list('test:list')
        n = 5
        for i in range(n):
            self.assertEqual(i, await test_list.size())
            await test_list.push_left('dummy_value_%s' % (i,))
        self.assertEqual(n, await test_list.size())

    @async_test
    async def test_right_pushing_preserves_order(self):
        redis = self._create_connection()
        test_list = redis.list('redis:list')
        await test_list.push_right(b'a', b'b', b'c')
        await test_list.push_right(b'd', b'e')
        self.assertEqual([b'a', b'b', b'c', b'd', b'e'], await test_list.list())

    @async_test
    async def test_left_pushing_preserves_inverse_order(self):
        redis = self._create_connection()
        test_list = redis.list('redis:list')
        await test_list.push_left(b'a', b'b', b'c')
        await test_list.push_left(b'd', b'e')
        self.assertEqual([b'e', b'd', b'c', b'b', b'a'], await test_list.list())

    @async_test
    async def test_removed_elements_are_not_contained_in_list(self):
        redis = self._create_connection()
        test_list = redis.list('redis:list')
        await test_list.push_right(b'a', b'b', b'c', b'd', b'e')
        await test_list.remove(b'b')
        await test_list.remove(b'c')
        await test_list.remove(b'e')
        self.assertEqual([b'a', b'd'], await test_list.list())
