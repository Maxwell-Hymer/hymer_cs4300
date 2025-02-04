import task1
import task2
import task3
import task4
import task5
import task6
import task7

# Test task1 and capture the standard output using capfd
def test_task1(capfd):
    # Run task1 and capture the standard output using capfd
    task1.main()
    captured = capfd.readouterr()

    # Test the standard output from capfd to see if it's correct
    assert captured.out.strip() == "Hello, World!"

# Tests for task2
def test_integer_demo():
    assert task2.integers_demo(3, 5) == 8

def test_floating_value_demo():
    assert task2.floating_value_demo(2.5, -1.15) == -2.875

def test_string_demo():
    assert task2.string_demo("Hello", "Max") == "Hello, Max!"

def test_boolean_demo():
    assert task2.boolean_demo(True, False) is True

# Tests for task 3
def test_if_statement_demo():
    assert task3.if_statement_demo(-3) == "Negative"
    assert task3.if_statement_demo(5) == "Positive"
    assert task3.if_statement_demo(0) == "Zero"


def test_for_loop_demo():
    assert task3.for_loop_demo() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_while_loop_demo():
    assert task3.while_loop_demo() == 5050

# Tests for task 4
def test_calculate_discount():
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(100.0, 20.0) == 80.0
    assert task4.calculate_discount(200, 15.5) == 169.0
    assert task4.calculate_discount(150.75, 10) == 135.675

# Tests for task 5
def test_favorite_books():
    expected_books = [
        {"title": "ATTACHMENT THEORY A Guide to Strengthening the Relationships in Your Life", "author": "Thais Gibson"},
        {"title": "THE BODY KEEPS THE SCORE", "author": "Bessel Van Der Kolk, M.D."},
        {"title": "The Freedom Model", "author": "Michelle Dunbar, Mark Scheeren, Steven Slate"}
    ]
    assert task5.favorite_books_demo() == expected_books

def test_student_database():
    expected_database = {
        "student1" : {"name": "Max", "student_id": "00001"},
        "student2" : {"name": "Jim", "student_id": "00002"},
        "student3" : {"name": "Steve", "student_id": "00003"}
    }
    assert task5.student_database_demo() == expected_database

# Task 6 test case
def test_read_me_word_count():
    # Define expected word counts for each text file
    expected_word_counts = {
        'task6_read_me.txt': 127,
    }

    # Dynamically create test functions for each text file
    for filename, expected_count in expected_word_counts.items():
        def make_test_function(filename, expected_count):
            def test_word_count():
                assert count_words_in_file(filename) == expected_count
            return test_word_count

        # Create a unique function name for each test
        test_func_name = f'test_word_count_{filename.replace(".", "_")}'
        globals()[test_func_name] = make_test_function(filename, expected_count)

# Task 7 test case
def test_numpy_demo():
    data_type = task7.numpy_demo(3, 6)
    assert data_type == "int64"