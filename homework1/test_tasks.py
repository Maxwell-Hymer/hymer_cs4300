import task1
import task2

# Test task1 and capture the standard output using capfd
def test_task1(capfd):
    # Run task1 and capture the standard output using capfd
    task1.main()
    captured = capfd.readouterr()

    # Test the standard output from capfd to see if it's correct
    assert captured.out.strip() == "Hello, World!"

# Tests for task2
def test_integer_demo():
    assert task2.integers_demo() == 8

def test_floating_value_demo():
    assert task2.floating_value_demo() == -2.875

def test_string_demo():
    assert task2.string_demo() == "Hello, Max!"

def test_boolean_demo():
    assert task2.boolean_demo() is True


