class RedisObject:
    def __init__(self, *, connection=None, key=None):
        self.connection = connection
        self.key = key

    async def watch(self, *, tx=None):
        tx = tx or self.connection
        await tx.execute('watch', self.key)

    async def unwatch(self, *, tx=None):
        tx = tx or self.connection
        await tx.execute('unwatch', self.key)
