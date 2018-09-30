import redisobjects
import asyncio

from redisobjects.mapper import *

class DummyObject:
    model = {
        'name': AtomMapper(),
        'friends': SetMapper(),
    }

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    object_space = redis.object_space('test.dummyobject', DummyObject)
    o = await object_space.create(DummyObject)
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
