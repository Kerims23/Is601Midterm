'''tests/test_history.py'''
import os
import pytest
from dotenv import load_dotenv
from faker import Faker
from app.commands.history import HistoryManager

load_dotenv()  # Load environment variables for tests

fake = Faker()  # Initialize a Faker instance

@pytest.fixture
def history_manager(tmp_path):
    """Fixture for creating a HistoryManager with a temporary file."""
    filename = tmp_path / os.getenv('HISTORY_FILE', 'test_history.csv')
    manager = HistoryManager(filename)
    return manager

@pytest.fixture
def mock_data():
    """Generate a list of mock history records."""
    return [
        {
            'index': i,
            'name': fake.name(),
            'operation': fake.random_element(elements=('add', 'subtract', 'multiply', 'divide')),
            'result': fake.random_number(digits=3)
        }
        for i in range(10)  # Generate 10 records
    ]

def test_save_multiple_records(history_manager, mock_data):
    """Test saving multiple records to the history."""
    for data in mock_data:
        history_manager.save(data)

    df = history_manager.load()
    assert len(df) == 10, "There should be 10 entries in the history file."

    for i, data in enumerate(mock_data):
        assert df.iloc[i]['name'] == data['name'], f"Record {i} should match the saved data."

def test_load_empty_file(history_manager):
    """Test loading from an empty file."""
    with open(history_manager.filename, 'w', encoding='utf-8') as f:
        pass  # Create an empty file

    df = history_manager.load()
    assert df.empty, "Loading from an empty file should return an empty DataFrame."

# Additional tests...
