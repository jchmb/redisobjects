import redisobjects
import asyncio

async def main():
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost')
    keyspace = redis.keyspace('test:?')
    l = keyspace.list('1')
    # Show that the list is empty from the start
    print(list(await l.items()))
    # Add values => [b] => [b, c] => [a, b, c]
    await l.push_right('b')
    await l.push_right('c')
    await l.push_left('a')
    # Show that the list is [a,b,c]
    print(list(await l.items()))
    # Pop c
    print(await l.pop_right())
    # Pop a
    print(await l.pop_left())
    # Pop b
    print(await l.pop_right())
    # Show that the list is empty
    print(list(await l.items()))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
