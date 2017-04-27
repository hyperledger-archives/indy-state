import pytest


@pytest.fixture(scope='function')
def tempdir(tmpdir_factory):
    return tmpdir_factory.mktemp('').strpath

from state.test.helper import empty_state as es


@pytest.fixture(scope='module')
def empty_state():
    return es()
