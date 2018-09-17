from .serializer import IdentitySerializer

class RedisKeyspace:
    def __init__(self, connection, keyspace='?', *key_serializers=[IdentitySerializer()]):
        self.connection = connection
        self.keyspace = keyspace
        self.key_serializers = key_serializers
        self.placeholder = '?'

    def _make_key(self, *keys):
        key = self.keyspace
        for i in range(len(keys)):
            key = key.replace(self.placeholder, self.key_serializers[i](keys[i]))
        if self.placeholder in self.keyspace:
            raise RuntimeError('Not all placeholders have been replaced for `%s`' % (key,))
        return key

    def state(self, *keys, value_serializer=IdentitySerializer()):
        key = self._make_key(*keys)
        return RedisState(self.connection, key, value_serializer)
