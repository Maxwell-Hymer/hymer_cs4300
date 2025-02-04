import task1
import task2
import task3

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

# Tests for task 3
def test_if_statement_demo():
    assert task3.if_statement_demo() == "Negative"

def test_for_loop_demo():
    assert task3.for_loop_demo() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_while_loop_demo():
    assert task3.while_loop_demo() == 5050


