import redisobjects
import asyncio

async def main():
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost')
    keyspace = redis.keyspace('test:?')
    s = keyspace.set('s') # the main set
    t = keyspace.set('t') # the secondary set
    # The set is empty
    print(set(await s.items()))
    # Add a,b,c to the set
    await s.add('a', 'b', 'c')
    # Show that {a,b,c} is the set
    print(set(await s.items()))
    # Add b,c,d to the secondary set
    await t.add('b', 'c', 'd')
    # Show that {b,c,d} is the secondary set
    print(set(await s.items()))
    # Show that the intersection of s and t is {b,c}
    print(set(await s.intersect(t)))
    # Pick two items at random with repetition
    print(await s.choose(4, False))
    # Remove c
    await s.remove('c')
    # Show that {a,b} is left
    print(set(await s.items()))
    # Remove a,b
    await s.remove('a', 'b')
    # Show that the set is empty again.
    print(set(await s.items()))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
