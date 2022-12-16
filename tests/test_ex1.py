import pytest

@pytest.fixture(scope="session")
def fixture_1():
    print('run-fixture-1')
    return 1

@pytest.mark.skip
def test_example():
    print("test")
    assert 1 == 1

@pytest.mark.slow
def test_example1(fixture_1):
    print("test 1")
    num = fixture_1
    assert 1 == num

def test_example2(fixture_1):
    print("test 2")
    num = fixture_1
    assert 1 == num



