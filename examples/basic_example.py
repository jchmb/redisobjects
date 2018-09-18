import redisobjects
import asyncio

async def main():
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost')
    keyspace = redis.keyspace('test:?')
    atom1 = keyspace.atom('1')
    atom2 = keyspace.atom('2')
    # Show that the values are not set.
    print(await atom1.get())
    print(await atom2.get())
    # Change the values.
    await atom1.set('abc')
    await atom2.set('xyz')
    # Demonstrate that the values have changed
    print(await atom1.get())
    print(await atom2.get())
    # Clean up
    await atom1.remove()
    await atom2.remove()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
