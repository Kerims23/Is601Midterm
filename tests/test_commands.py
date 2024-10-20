'''tests/test_commands.py'''
# tests/test_command_handler.py
import pytest
from app.commands import CommandHandler
from faker import Faker

fake = Faker()

@pytest.fixture
def command_handler_fixture():
    """Fixture for the CommandHandler."""
    return CommandHandler()

def test_execute_operation_add(command_handler_fixture, random_numbers):
    """Test addition operation in CommandHandler."""
    for a, b in random_numbers:
        result = command_handler_fixture.execute_operation("add", a, b)
        assert result == a + b

def test_execute_operation_subtract(command_handler_fixture, random_numbers):
    """Test subtraction operation in CommandHandler."""
    for a, b in random_numbers:
        result = command_handler_fixture.execute_operation("subtract", a, b)
        assert result == a - b

def test_execute_operation_multiply(command_handler_fixture, random_numbers):
    """Test multiplication operation in CommandHandler."""
    for a, b in random_numbers:
        result = command_handler_fixture.execute_operation("multiply", a, b)
        assert result == a * b

def test_execute_operation_divide(command_handler_fixture, random_numbers):
    """Test division operation in CommandHandler."""
    for a, b in random_numbers:
        if b != 0:  # Avoid division by zero
            result = command_handler_fixture.execute_operation("divide", a, b)
            assert result == a / b
        else:
            with pytest.raises(ZeroDivisionError):
                command_handler_fixture.execute_operation("divide", a, b)

def test_save_and_load_history(command_handler_fixture, random_numbers):
    """Test saving and loading history in CommandHandler."""
    for idx, (a, b) in enumerate(random_numbers):
        data = {
            'index': idx,
            'name': fake.name(),
            'operation': 'add',
            'result': a + b
        }
        command_handler_fixture.save_history(data)

    # Load history and verify
    history = command_handler_fixture.load_history()
    assert len(history) == len(random_numbers)
    for idx, row in history.iterrows():
        assert row['operation'] == 'add'

def test_delete_history(command_handler_fixture, random_numbers):
    """Test deleting history in CommandHandler."""
    for idx, (a, b) in enumerate(random_numbers):
        data = {
            'index': idx,  
            'name': fake.name(),
            'operation': 'add',
            'result': a + b
        }
        command_handler_fixture.save_history(data)

    # Load history before deletion
    history_before = command_handler_fixture.load_history()
    print("History before deletion:", history_before)

    # Delete the first entry and verify
    command_handler_fixture.delete_history(0)  # Deleting the first entry
    history_after = command_handler_fixture.load_history()
    print("History after deletion:", history_after)

    # Assert that history length is now one less than before
    assert len(history_after) == len(history_before) - 1  # One less entry


def test_clear_history(command_handler_fixture, random_numbers):
    """Test clearing history in CommandHandler."""
    for idx, (a, b) in enumerate(random_numbers):
        data = {
            'index': idx + 1,
            'name': fake.name(),
            'operation': 'add',
            'result': a + b
        }
        command_handler_fixture.save_history(data)

    # Clear history and verify
    command_handler_fixture.clear_history()
    history = command_handler_fixture.load_history()
    assert history.empty
