import redisobjects
import asyncio

async def main(loop):
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    s = redis.set('example:set:s') # the main set
    t = redis.set('example:set:t') # the secondary set
    print(set(await s.items()))
    await s.add('a', 'b', 'c')
    print(set(await s.items()))
    await t.add('b', 'c', 'd')
    print(set(await s.items()))
    print(set(await s.intersect(t)))
    print(await s.choose(4, False))
    await s.remove('c')
    print(set(await s.items()))
    await s.remove('a', 'b')
    print(set(await s.items()))
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
