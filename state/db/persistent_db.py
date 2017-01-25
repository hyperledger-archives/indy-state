import leveldb

from state.db.db import BaseDB


class PeristentDB(BaseDB):
    def __init__(self, dbPath):
        self.db = leveldb.LevelDB(dbPath)
        self.kv = self.db

    def get(self, key: bytes) -> bytes:
        return self.db.Get(key)

    def put(self, key: bytes, value: bytes):
        self.db.Put(key, value)

    def delete(self, key: bytes):
        self.db.Delete(key)

    # def commit(self):
    #     pass

    def _has_key(self, key: bytes):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __contains__(self, key):
        return self._has_key(key)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.db == other.db

    # def __hash__(self):
    #     return utils.big_endian_to_int(str_to_bytes(self.__repr__()))
    #
    # def inc_refcount(self, key, value):
    #     self.put(key, value)
    #
    # def dec_refcount(self, key):
    #     pass
    #
    # def revert_refcount_changes(self, epoch):
    #     pass
    #
    # def commit_refcount_changes(self, epoch):
    #     pass

    def cleanup(self, epoch):
        pass

    # def put_temporarily(self, key, value):
    #     self.inc_refcount(key, value)
    #     self.dec_refcount(key)
