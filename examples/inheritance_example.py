import redisobjects
from redisobjects import RedisAtom
import asyncio

class Animal:
    def __init__(self):
        self.name = RedisAtom()

class Pet(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.owner = RedisAtom()

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    entity_space = redis.entity_space('example:animal', Animal)
    a = await entity_space.create(Animal)
    b = await entity_space.create(Pet)
    await a.name.set('Bobby')
    await b.name.set('Timmy')
    await b.owner.set('Owner-Man')
    aa = await entity_space.object(a._id)
    bb = await entity_space.object(b._id)
    print(await aa.name.get())
    print(await bb.name.get())
    print(aa.__class__.__name__)
    print(bb.__class__.__name__)
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
