import redisobjects
import asyncio

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    list = redis.list('example.list')
    atom = redis.atom('example.atom')
    tx = redis.create_transaction()
    await list.push_right('a', 'b', tx=tx)
    await atom.set('a', tx=tx)
    print(await list.list())
    print(await atom.get())
    await tx.commit()
    print(await list.list())
    print(await atom.get())
    # Clean up
    await list.remove('a')
    await list.remove('b')
    await atom.remove()
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
