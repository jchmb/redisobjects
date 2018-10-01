import redisobjects
import asyncio

from redisobjects.mapper import *

class Animal:
    model = {
        'name': IndexMapper(),
        'favorite_color': AtomMapper(),
    }

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    object_space = redis.object_space('test.animal', Animal)
    a = await  object_space.create(Animal)
    await a.name.set('Alice')
    await a.favorite_color.set('red')
    b = await object_space.create(Animal)
    await b.name.set('Bob')
    await b.favorite_color.set('green')
    aa = await object_space.find('name', 'Alice')
    bb = await object_space.find('name', 'Bob')
    print(await aa.name.get())
    print(await bb.name.get())
    print(await aa.favorite_color.get())
    print(await bb.favorite_color.get())
    await object_space.remove(aa)
    await object_space.remove(bb)
    print(await aa.name.get())
    print(await bb.name.get())
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
