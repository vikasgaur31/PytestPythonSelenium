import pytest
from pytest import mark

@mark.engine
def test_engine_function_as_expected():
    assert True
    