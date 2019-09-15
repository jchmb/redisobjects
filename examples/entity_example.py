import redisobjects
import asyncio

from redisobjects import RedisAtom, RedisSet

class DummyEntity:
    def __init__(self):
        self.name = RedisAtom()
        self.friends = RedisSet()

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    entity_space = redis.entity_space('test:dummy-entity', DummyEntity)
    o = await entity_space.create(DummyEntity)
    await o.name.set('Jochem')
    await o.friends.add('Bob')
    await o.friends.add('Tom')
    await o.friends.add('Jerry')
    print(await o.name.get())
    print(await o.friends.set())
    await object_space.remove(o)
    print(await o.name.get())
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
