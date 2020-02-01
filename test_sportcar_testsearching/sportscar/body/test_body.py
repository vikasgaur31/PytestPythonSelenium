import pytest
from pytest import mark

@mark.smoke
@mark.body
def test_body_function_as_expected():
    assert True

def test_body_function_as_expected1():
    assert True
