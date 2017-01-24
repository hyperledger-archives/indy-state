import patricia.trie.pruning_trie as trie
from patricia.trie.refcount_db import RefcountDB
from patricia.trie.db import EphemDB


def empty_state():
    root = trie.BLANK_ROOT
    db1 = RefcountDB(EphemDB())
    return trie.Trie(db1, root)
