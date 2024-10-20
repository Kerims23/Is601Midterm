'''tests/test_history.py'''
import pandas as pd
from faker import Faker
import pytest
from app.commands.history import HistoryManager

fake = Faker()

@pytest.fixture
def history_manager_fixture(tmp_path):
    """Fixture for HistoryManager, using a temporary file."""
    filename = tmp_path / "history.csv"
    return HistoryManager(filename)

def test_save(history_manager_fixture):
    """Test saving an entry to history."""
    data = {
        'index': 1,
        'name': fake.name(),
        'operation': 'add',
        'result': fake.random_number(digits=3)
    }
    history_manager_fixture.save(data)

    # Load the data to verify
    loaded_df = history_manager_fixture.load()
    assert len(loaded_df) == 1
    assert loaded_df.iloc[0]['name'] == data['name']
    assert loaded_df.iloc[0]['operation'] == data['operation']
    assert loaded_df.iloc[0]['result'] == data['result']

def test_load_empty_file(history_manager_fixture):
    """Test loading from an empty history file."""
    loaded_df = history_manager_fixture.load()
    assert loaded_df.empty

def test_delete(history_manager_fixture):
    """Test deleting an entry from history."""
    data1 = {
        'index': 1,
        'name': fake.name(),
        'operation': 'add',
        'result': fake.random_number(digits=3)
    }
    data2 = {
        'index': 2,
        'name': fake.name(),
        'operation': 'subtract',
        'result': fake.random_number(digits=3)
    }
    history_manager_fixture.save(data1)
    history_manager_fixture.save(data2)

    # Delete the first entry
    history_manager_fixture.delete(0)
    loaded_df = history_manager_fixture.load()
    assert len(loaded_df) == 1
    assert loaded_df.iloc[0]['name'] == data2['name']  # Ensure the second entry remains

def test_delete_invalid_index(history_manager_fixture):
    """Test deleting with an invalid index."""
    history_manager_fixture.save({
        'index': 1,
        'name': fake.name(),
        'operation': 'add',
        'result': fake.random_number(digits=3)
    })
    history_manager_fixture.delete(5)  # Attempt to delete a non-existent index
    loaded_df = history_manager_fixture.load()
    assert len(loaded_df) == 1  # Ensure that the entry is still there

def test_clear(history_manager_fixture):
    """Test clearing the history."""
    data = {
        'index': 1,
        'name': fake.name(),
        'operation': 'add',
        'result': fake.random_number(digits=3)
    }
    history_manager_fixture.save(data)
    history_manager_fixture.clear()
    loaded_df = history_manager_fixture.load()
    assert loaded_df.empty  # The history should be empty after clearing

