Redisobjects
============

Simple wrapper for [aioredis](https://github.com/aio-libs/aioredis) to provide asynchronous functionality with a clean object-oriented interface for Redis in Python 3.6+.

Installation
------------

```shell
pip install redisobjects
```

Examples
--------

```python
import redisobjects
import asyncio

async def main(loop):
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    keyspace = redis.keyspace('?')
    atom = keyspace.atom('test')
    # Show that the value is not set.
    print(await atom.get())
    # Change the value.
    await atom.set('abc')
    # Demonstrate that the value has changed
    print(await atom.get())
    # Clean up
    await atom.remove()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
```
