'''tests/test_operations.py'''
import pytest
from app.plugins.operations import Operations
# this is to stop the error
# pylint: disable=redefined-outer-name
@pytest.fixture
def operations():
    '''passing operations'''
    return Operations()

def test_add(operations, a, b):
    '''addition tests'''
    result = operations.add(a, b)
    assert result == a + b

def test_subtract(operations, a, b):
    '''subtraction tests'''
    result = operations.subtract(a, b)
    assert result == a - b

def test_multiply(operations, a, b):
    '''multiplication tests'''
    result = operations.multiply(a, b)
    assert result == a * b

def test_divide(operations, a, b):
    '''division tests'''
    if b != 0:
        result = operations.divide(a, b)
        assert result == a / b
    else:
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            operations.divide(a, b)
