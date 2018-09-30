import redisobjects
import asyncio

from redisobjects.mapper import *

class Animal:
    model = {
        'name': AtomMapper(),
    }

class Pet(Animal):
    model = {
        **Animal.model,
        'owner': AtomMapper(),
    }

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    object_space = redis.object_space('test.animal', Animal)
    a = await object_space.create(Animal)
    b = await object_space.create(Pet)
    await a.name.set('Bobby')
    await b.name.set('Timmy')
    await b.owner.set('Owner-Man')
    aa = await object_space.object(a._id)
    bb = await object_space.object(b._id)
    print(await aa.name.get())
    print(await bb.name.get())
    print(aa.__class__.__name__)
    print(bb.__class__.__name__)
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
