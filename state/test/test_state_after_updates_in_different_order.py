from state.test.helper import empty_state
from state.util.fast_rlp import encode_optimized as rlp_encode


def test_state_after_updates_in_different_order():
    state1 = empty_state()

    state1.update('k1'.encode(), rlp_encode(['v1']))
    state1.update('k2'.encode(), rlp_encode(['v2']))
    state1.update('k1'.encode(), rlp_encode(['v1a']))
    state1.update('k3'.encode(), rlp_encode(['v3']))
    state1.delete('k2'.encode())

    state2 = empty_state()

    state2.update('k1'.encode(), rlp_encode(['v1a']))
    state2.update('k3'.encode(), rlp_encode(['v3']))

    print(state1.get_root_hash())
    print(state2.get_root_hash())

    assert state1.get_root_hash() == state2.get_root_hash()
