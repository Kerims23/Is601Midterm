# tests/test_operations.py
import pytest
from app.commands.operations import Operations

@pytest.fixture
def operations():
    """Fixture for Operations class."""
    return Operations()

def test_operations_add(operations, a, b):
    """Test addition operation."""
    result = operations.add(a, b)
    assert result == a + b, f"Expected {a + b}, but got {result}"

def test_operations_multiply(operations, a, b):
    """Test multiplication operation."""
    result = operations.multiply(a, b)
    assert result == a * b, f"Expected {a * b}, but got {result}"

def test_operations_divide_by_zero(operations):
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        operations.divide(1, 0)
