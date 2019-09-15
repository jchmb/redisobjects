import redisobjects
from redisobjects import RedisAtom, indexed
import asyncio

class Animal:
    def __init__(self):
        @indexed
        self.name = RedisAtom()
        self.favorite_color = RedisAtom()

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    entity_space = redis.entity_space('example:animal', Animal)
    a = await  entity_space.create(Animal)
    await a.name.set('Alice')
    await a.favorite_color.set('red')
    b = await entity_space.create(Animal)
    await b.name.set('Bob')
    await b.favorite_color.set('green')
    aa = await entity_space.find('name', 'Alice')
    bb = await entity_space.find('name', 'Bob')
    print(await aa.name.get())
    print(await bb.name.get())
    print(await aa.favorite_color.get())
    print(await bb.favorite_color.get())
    await entity_space.remove(aa)
    await entity_space.remove(bb)
    print(await aa.name.get())
    print(await bb.name.get())
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
