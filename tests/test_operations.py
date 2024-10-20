# tests/test_operations.py
import pytest
from app.commands.operations import Operations

@pytest.fixture
def operations():
    return Operations()

def test_add(operations, a, b):
    result = operations.add(a, b)
    assert result == a + b

def test_subtract(operations, a, b):
    result = operations.subtract(a, b)
    assert result == a - b

def test_multiply(operations, a, b):
    result = operations.multiply(a, b)
    assert result == a * b

def test_divide(operations, a, b):
    if b != 0:
        result = operations.divide(a, b)
        assert result == a / b
    else:
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            operations.divide(a, b)
