import state.trie.pruning_trie as trie
from state.util.fast_rlp import encode_optimized as rlp_encode, \
    decode_optimized as rlp_decode


def test_get_values_at_roots(empty_state):
    # Update key with different values but preserve root after each update
    # Check values of keys with different previous roots and check that they
    # are correct
    state = empty_state

    state.update('k1'.encode(), rlp_encode(['v1']))
    # print state.root_hash.encode('hex')
    # print state.root_node

    val = state.get('k1')
    print(rlp_decode(val))
    oldroot1 = state.root_node
    old_root1_hash = state.root_hash
    assert state._decode_to_node(old_root1_hash) == oldroot1
    state.update('k1'.encode(), rlp_encode(['v1a']))
    val = state.get('k1')
    assert rlp_decode(val) == [b'v1a', ]

    # Already saved roots help in getting previous values
    oldval = state.get_at(oldroot1, 'k1')
    assert rlp_decode(oldval) == [b'v1', ]
    oldroot1a = state.root_node

    state.update('k1'.encode(), rlp_encode([b'v1b']))
    val = state.get('k1')
    assert rlp_decode(val) == [b'v1b']

    oldval = state.get_at(oldroot1a, 'k1')
    assert rlp_decode(oldval) == [b'v1a', ]

    oldval = state.get_at(oldroot1, 'k1')
    assert rlp_decode(oldval) == [b'v1', ]

    oldroot1b = state.root_node

    state.update('k1'.encode(), rlp_encode([b'v1c']))
    val = state.get('k1')
    assert rlp_decode(val) == [b'v1c', ]

    oldval = state.get_at(oldroot1b, 'k1')
    assert rlp_decode(oldval) == [b'v1b', ]

    oldval = state.get_at(oldroot1a, 'k1')
    assert rlp_decode(oldval) == [b'v1a', ]

    oldval = state.get_at(oldroot1, 'k1')
    assert rlp_decode(oldval) == [b'v1', ]

    oldroot1c = state.root_node

    state.delete('k1'.encode())
    assert state.get('k1') == trie.BLANK_NODE

    oldval = state.get_at(oldroot1c, 'k1')
    assert rlp_decode(oldval) == [b'v1c', ]

    oldval = state.get_at(oldroot1b, 'k1')
    assert rlp_decode(oldval) == [b'v1b', ]

    oldval = state.get_at(oldroot1a, 'k1')
    assert rlp_decode(oldval) == [b'v1a', ]

    oldval = state.get_at(oldroot1, 'k1')
    assert rlp_decode(oldval) == [b'v1', ]

    state.root_node = oldroot1c
    val = state.get('k1')
    assert rlp_decode(val) == [b'v1c', ]

    state.root_node = oldroot1
    val = state.get('k1')
    assert rlp_decode(val) == [b'v1', ]
