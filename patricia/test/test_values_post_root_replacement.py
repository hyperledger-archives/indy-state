import patricia.trie.pruning_trie as trie
from patricia.trie.db import EphemDB
from patricia.trie.fast_rlp import encode_optimized as rlp_encode
from patricia.trie.refcount_db import RefcountDB


def test_values_post_root_replacement(empty_state):
    state = empty_state

    for i in range(1, 5):
        state.update('k{}'.format(i).encode(), rlp_encode(['v{}'.format(i)]))

    root1 = state.root_node

    for i in range(1, 5):
        state.update('k{}'.format(i).encode(), rlp_encode(['vv{}'.format(i)]))

    root2 = state.root_node

    print("Updated values")
    for i in range(1, 5):
        print(state.get('k{}'.format(i)))

    print("Values according to old root")
    old_values = {}
    for i in range(1, 5):
        key = 'k{}'.format(i)
        val = state.get_at(root1, key)
        old_values[key] = val
        print(val)

    print("Values after replacing new root with old root")
    state.replace_root_hash(root2, root1)

    for i in range(1, 5):
        key = 'k{}'.format(i)
        val = state.get_at(root1, key)
        print(val)
        assert old_values[key] == val
