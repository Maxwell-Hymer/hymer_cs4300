import task1

def test_tasks(capfd):
    # Test task1 and capture the standard output using capfd
    task1.main()
    captured = capfd.readouterr()

    # Test the standard output from capfd to see if it's correct
    assert captured.out.strip() == "Hello, World!"

    

