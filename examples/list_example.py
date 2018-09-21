import redisobjects
import asyncio

async def main(loop):
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    example_list = redis.list('example.list')
    print(await example_list.list())
    await example_list.push_right('b')
    await example_list.push_right('c')
    print(await example_list.list())
    await example_list.push_left('a')
    print(await example_list.list())
    await example_list.pop_left()
    await example_list.pop_left()
    print(await example_list.list())
    await example_list.pop_left()
    print(await example_list.list())
    redis.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
