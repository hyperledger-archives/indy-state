import pytest

from state.test.helper import empty_state as es


@pytest.fixture(scope='module')
def empty_state():
    return es()

