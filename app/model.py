from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Product(Model):
    __keyspace__ = ''