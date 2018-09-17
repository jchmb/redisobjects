from .redis_keyspace import RedisKeyspace
from .serializer import IdentitySerializer

class RedisManager:
    def __init__(self, connection):
        self.connection = connection

    def keyspace(self, keyspace, *key_serializers=[IdentitySerializer()]):
        return RedisKeyspace(self.connection, keyspace, *key_serializers)
