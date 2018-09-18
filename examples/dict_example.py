import redisobjects
import asyncio

async def main():
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost')
    keyspace = redis.keyspace('test:?')
    d = keyspace.dict('1')
    # Show that the dict is empty
    print(dict(await d.items()))
    # Set a = 1
    await d.set('a', '1')
    # Show that the dict contains {a:1}
    print(dict(await d.items()))
    # Set b = 2
    await d.set('b', '2')
    # Show that the dict contains {b:2}
    print(dict(await d.items()))
    # Set c = 3
    await d.set('c', '3')
    # Show that the dict contains {a:1,b:2,c:3}
    print(dict(await d.items()))
    # Remove a and b
    await d.remove('a', 'b')
    # Show that only {c:3} remains.
    print(dict(await d.items()))
    # Remove c
    await d.remove('c')
    # Show that the dict is empty
    print(dict(await d.items()))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
