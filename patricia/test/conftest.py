import pytest

import patricia.trie.pruning_trie as trie
from patricia.trie.refcount_db import RefcountDB
from patricia.trie.db import EphemDB
from patricia.test.helper import empty_state as es


@pytest.fixture(scope='module')
def empty_state():
    return es()

