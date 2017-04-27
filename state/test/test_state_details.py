from state.util.fast_rlp import encode_optimized as rlp_encode, \
    decode_optimized as rlp_decode


def testStateDetails(empty_state):
    state = empty_state

    state.update('k1'.encode(), rlp_encode(['v1']))
    root1 = state.root_node
    state.update('k2'.encode(), rlp_encode(['v2']))
    root2 = state.root_node
    state.update('k3'.encode(), rlp_encode(['v3']))
    root3 = state.root_node

    print(root1)
    print(root2)
    print(root3)

    print(state._get_size(root3))
    assert state._get_size(root3) == 3
    print(state._get_size(root2))
    # assert state._get_size(root2) == 2
    print(state._get_size(root1))
    # assert state._get_size(root1) == 1

    print(state._to_dict(root3))
    print(state._to_dict(root2))
    print(state._to_dict(root1))

    print(state.to_dict())

    data = {k: rlp_decode(v) for k, v in state.to_dict().items()}
    print(data)

    assert data == {b'k1': [b'v1',], b'k2': [b'v2',], b'k3': [b'v3',]}