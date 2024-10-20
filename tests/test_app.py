'''tests/test_app.py'''
import os
from unittest.mock import patch
from dotenv import load_dotenv
import pandas as pd
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

def test_app_operations_all(app_fixture):
    """Test all basic operations of the app."""
    assert app_fixture.command_handler.execute_operation('add', 5, 3) == 8
    assert app_fixture.command_handler.execute_operation('subtract', 10, 4) == 6
    assert app_fixture.command_handler.execute_operation('multiply', 2, 3) == 6
    assert app_fixture.command_handler.execute_operation('divide', 10, 2) == 5

def test_app_invalid_operations(app_fixture):
    """Test handling of invalid operations."""
    with pytest.raises(ValueError):
        app_fixture.command_handler.execute_operation('invalid_command', 5, 3)

def test_app_divide_by_zero(app_fixture):
    """Test the divide by zero scenario."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        app_fixture.command_handler.execute_operation('divide', 10, 0)

def test_last_result_initialization():
    """Test that last_result is initialized to None."""
    app_fixture = App()  # Instantiate the App
    assert app_fixture.last_result is None  # Check if last_result is None

def test_history_file_path():
    """Test that the history_file is initialized correctly."""
    app_fixture = App()  # Instantiate the App
    assert app_fixture.history_file == "data/account.csv"

def test_initialization_creates_csv(app_fixture):
    """Test that CSV file is created with headers on initialization."""
    assert os.path.exists(app_fixture.history_file)
    history_df = pd.read_csv(app_fixture.history_file)
    assert list(history_df.columns) == ['index', 'name', 'operation', 'result']

def test_clear_history(app_fixture, capfd):
    """Test the clear history functionality."""
    # Mock user input for starting the app and issuing a clear command
    with patch('builtins.input', side_effect=['Test User', 'clear', 'exit']):
        # Start the app
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
        "History cleared.\n"
    )
    assert captured.out == expected_output

def test_delete_nonexistent_history(app_fixture, capfd):
    """Test deleting a nonexistent history entry."""
    # Mock user input for starting the app and issuing a delete command
    with patch('builtins.input', side_effect=['Test User', 'delete', '0', 'exit']):
            # Simulate no records in history
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
        "Error: No records found in history to delete.\n"
    )
    assert captured.out == expected_output

def test_load_history_empty(app_fixture, capfd):
    """Test loading history when empty."""
    with patch('builtins.input', side_effect=['Test User', 'load', 'exit']):
            # Simulate no records in history
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
        "History is empty.\n"
    )
    assert captured.out == expected_output

def test_start_greeting_message(app_fixture, capfd):
    """Test greeting message."""
    with patch('builtins.input', side_effect=['Test User', 'exit']):
            # Simulate no records in history
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
    )
    assert captured.out == expected_output

def test_save_history_with_result(app_fixture, capfd):
    """Test saving history with a valid result."""
    with patch('builtins.input', side_effect=['Test User', 'add', '1', '2', 'save', 'exit']):
            # Simulate no records in history
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
        "Result: 3.0\n"
        "History saved.\n"
    )
    assert captured.out == expected_output

def test_save_history_without_result(app_fixture, capfd):
    """Test saving history without a result."""
    with patch('builtins.input', side_effect=['Test User', 'save', 'exit']):
            # Simulate no records in history
        app_fixture.start()
    # Capture the output
    captured = capfd.readouterr()
    # Check the output
    expected_output = (
        "Hello, Test User! You can now perform operations.\n"
        "No results to save. Please perform an operation first.\n"
    )
    assert captured.out == expected_output

def test_environment_variable():
    """Test if the correct environment is loaded."""
    # Manually specify the .env file path
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    # Check if the .env file exists at the specified path
    assert os.path.exists(env_path), f".env file not found at {env_path}"
    # Load the .env file
    load_dotenv(env_path)
    # Print to check if the variable is loaded
    print(f"ENVIRONMENT: {os.getenv('ENVIRONMENT')}")
    # Assert that the ENVIRONMENT variable is set to "development"
    assert os.getenv("ENVIRONMENT") == "development"
