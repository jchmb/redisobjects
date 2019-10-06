import unittest

from redisobjects import connect_fakeredis
from .async_test import async_test

class RedisSetTest(unittest.TestCase):
    @async_test
    async def test_new_set_is_empty(self):
        redis = connect_fakeredis()
        test_set = redis.set('test:set')
        self.assertEqual(0, await test_set.size())

    @async_test
    async def test_elements_added_are_contained_by_set(self):
        redis = connect_fakeredis()
        test_set = redis.set('test:set')
        n = 3
        for i in range(n):
            element = ('element_%s' % (i,)).encode()
            await test_set.add(element)
            self.assertTrue(await test_set.contains(element))

    @async_test
    async def test_removed_element_from_set_is_not_contained_by_set(self):
        redis = connect_fakeredis()
        test_set = redis.set('test:set')
        n = 5
        for i in range(n):
            element = ('element_%s' % (i,)).encode()
            await test_set.add(element)
            await test_set.remove(element)
            self.assertFalse(await test_set.contains(element))

    @async_test
    async def test_for_every_element_added_set_size_increases_by_one(self):
        redis = connect_fakeredis()
        test_set = redis.set('test:set')
        n = 4
        for i in range(n):
            element = ('element_%s' % (i,)).encode()
            self.assertEqual(i, await test_set.size())
            await test_set.add(element)
        self.assertEqual(n, await test_set.size())

    @async_test
    async def test_move_element_from_one_set_to_another_is_contained_only_by_latter(self):
        redis = connect_fakeredis()
        test_set_a = redis.set('test:set-a')
        test_set_b = redis.set('test:set-b')
        n = 3
        for i in range(n):
            element = ('element_%s' % (i,)).encode()
            await test_set_a.add(element)
            self.assertTrue(await test_set_a.contains(element))
            self.assertFalse(await test_set_b.contains(element))
            await test_set_a.move(element, test_set_b)
            self.assertFalse(await test_set_a.contains(element))
            self.assertTrue(await test_set_b.contains(element))

    @async_test
    async def test_union_of_set_a_and_b_yields_set_with_exactly_all_elements_from_both(self):
        redis = connect_fakeredis()
        test_set_a = redis.set('test:set-a')
        test_set_b = redis.set('test:set-b')
        await test_set_a.add(b'a', b'b')
        await test_set_b.add(b'b', b'c', b'd')
        expected = set([b'a', b'b', b'c', b'd'])
        self.assertEqual(expected, await test_set_a.union(test_set_b))
