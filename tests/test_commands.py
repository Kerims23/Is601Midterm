'''tests/test_commands.py'''
from app.commands import CommandHandler

def test_addition_command():
    """Test the addition operation."""
    command_handler = CommandHandler()
    result = command_handler.execute_operation("add", 2, 3)
    assert result == 5.0, f"Expected 5.0, but got {result}"

def test_subtraction_command():
    """Test the subtraction operation."""
    command_handler = CommandHandler()
    result = command_handler.execute_operation("subtract", 5, 3)
    assert result == 2.0, f"Expected 2.0, but got {result}"

# Add similar tests for multiplication and division commands
