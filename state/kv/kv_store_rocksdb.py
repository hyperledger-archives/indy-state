from typing import Iterable, Tuple

import shutil
from state.kv.kv_store import KeyValueStorage
from state.util.utils import removeLockFiles

try:
    import rocksdb
except ImportError:
    print('Cannot import rocksdb, please install')


class KeyValueStorageRocksdb(KeyValueStorage):
    def __init__(self, dbPath, open=True):
        if 'rocksdb' not in globals():
            raise RuntimeError('Rocksdb is needed to use this class')
        self._dbPath = dbPath
        self._db = None
        if open:
            self.open()

    def open(self):
        self._db = rocksdb.DB(self._dbPath, rocksdb.Options(create_if_missing=True))

    def __repr__(self):
        return self._dbPath

    def put(self, key, value):
        if isinstance(key, str):
            key = key.encode()
        if isinstance(value, str):
            value = value.encode()
        self._db.put(key, value)

    def get(self, key):
        if isinstance(key, str):
            key = key.encode()
        return self._db.get(key)

    def remove(self, key):
        if isinstance(key, str):
            key = key.encode()
        self._db.delete(key)

    def setBatch(self, batch: Iterable[Tuple]):
        b = rocksdb.WriteBatch()
        for key, value in batch:
            if isinstance(key, str):
                key = key.encode()
            if isinstance(value, str):
                value = value.encode()
            b.put(key, value)
        self._db.write(b, sync=False)

    def close(self):
        removeLockFiles(self._dbPath)
        del self._db
        self._db = None

    def drop(self):
        self.close()
        shutil.rmtree(self._dbPath)

    def iter(self, start=None, end=None, include_value=True):
        if not include_value:
            itr = self._db.iterkeys()
        else:
            itr = self._db.iteritems()
        itr.seek_to_first()
        return itr

    def has_key(self, key):
        if isinstance(key, str):
            key = key.encode()
        return self._db.key_may_exist(key)[0]
