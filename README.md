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

```python
import redisobjects
import asyncio

async def main(loop):
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    keyspace = redis.keyspace('?')
    l = keyspace.list('test')
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
loop.run_until_complete(main(loop))
loop.close()
```

```python
import redisobjects
import asyncio

async def main(loop):
    # Initialize and declare
    redis = await redisobjects.connect('redis://localhost', loop=loop)
    keyspace = redis.keyspace('?')
    d = keyspace.dict('test')
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
loop.run_until_complete(main(loop))
loop.close()
```
