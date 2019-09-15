import redisobjects
import asyncio

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    d = redis.dict('example:dict')
    print(dict(await d.items()))
    await d.set('a', '1')
    print(dict(await d.items()))
    await d.set('b', '2')
    print(dict(await d.items()))
    await d.set('c', '3')
    print(dict(await d.items()))
    await d.remove('a', 'b')
    print(dict(await d.items()))
    await d.remove('c')
    print(dict(await d.items()))
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
