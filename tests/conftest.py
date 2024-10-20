# tests/conftest.py
from faker import Faker
import pytest

fake = Faker()

@pytest.fixture
def random_numbers(num_records):
    """Fixture to generate a list of random (a, b) number tuples."""
    return [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(num_records)]

@pytest.fixture
def num_records(pytestconfig):
    """Fixture to get num_records value from command-line argument."""
    return pytestconfig.getoption("num_records")

def generate_test_data(num_records):
    """Generate test data for operations."""
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)  # You can adjust the range as needed
        b = fake.random_int(min=1, max=100)
        yield a, b

def pytest_addoption(parser):
    """Add command line options for pytest."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate.")

def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on the provided fixture names."""
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("a,b", parameters)
