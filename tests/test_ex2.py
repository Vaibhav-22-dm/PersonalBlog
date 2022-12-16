import pytest

@pytest.fixture
def yield_fixture():
    print('Start Test Phase')
    yield 6
    print('End Test Phase')

def test_example(yield_fixture):
    print("test")
    assert yield_fixture == 6