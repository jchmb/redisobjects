import redisobjects
import asyncio

async def main():
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost')
    keyspace = redis.keyspace('test:?')
    state1 = keyspace.state('1')
    state2 = keyspace.state('2')
    # Show that the values are not set.
    print(await state1.get())
    print(await state2.get())
    # Change the values.
    await state1.set('abc')
    await state2.set('xyz')
    # Demonstrate that the values have changed
    print(await state1.get())
    print(await state2.get())
    # Clean up
    await state1.remove()
    await state2.remove()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
