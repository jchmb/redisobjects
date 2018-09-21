import redisobjects
import asyncio

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    atom = redis.atom('example.atom')
    print(await atom.get())
    await atom.set('bla')
    print(await atom.get())
    await atom.remove()
    print(await atom.get())
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
