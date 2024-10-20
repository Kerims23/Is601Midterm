'''tests/test_app.py'''
import pytest
from app import App  # Import your App class
# this is to stop the error
# pylint: disable=redefined-outer-name
@pytest.fixture
def app_fixture():
    """Fixture to set up the App instance for testing."""
    app = App()  # Instantiate your app
    yield app  # Allow tests to run with this instance

def test_app_initialization(app_fixture):
    """Test that the app initializes correctly."""
    assert app_fixture is not None  # Check that the app instance is created
    assert app_fixture.history_file == "data/account.csv"  # Check history file path

def test_app_operations(app_fixture):
    """Test basic operations of the app."""
    result_add = app_fixture.command_handler.execute_operation('add', 5, 3)
    assert result_add == 8  # Check if addition works as expected

    result_subtract = app_fixture.command_handler.execute_operation('subtract', 10, 4)
    assert result_subtract == 6  # Check if subtraction works

def test_app_history_management(app_fixture):
    """Test the history management of the app."""
    app_fixture.command_handler.save_history({'index': 0,
                                              'name': 'Test', 'operation': 'add', 'result': 5})

    history = app_fixture.command_handler.load_history()
    assert len(history) == 1  # Verify the history has one entry

    app_fixture.command_handler.delete_history(0)  # Delete the entry
    history = app_fixture.command_handler.load_history()
    assert len(history) == 0  # Verify history is empty after deletion

def test_app_clear_history(app_fixture):
    """Test the clear history functionality."""
    app_fixture.command_handler.save_history({'index': 0,
                                              'name': 'Test', 'operation': 'add', 'result': 5})
    app_fixture.command_handler.clear_history()  # Clear the history
    history = app_fixture.command_handler.load_history()
    assert history.empty  # Verify history is empty after clearing
