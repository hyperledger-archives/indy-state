from state.db.refcount_db import RefcountDB

import state.trie.pruning_trie as trie
from state.db.db import EphemDB


def empty_state():
    root = trie.BLANK_ROOT
    db1 = RefcountDB(EphemDB())
    return trie.Trie(db1, root)
