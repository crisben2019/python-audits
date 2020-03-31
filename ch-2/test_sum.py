from src.sum import sum

def test_multiple_positive_numbers():
    assert sum(5, 2, 3) == 10

def test_multiple_negative_numbers():
    assert sum(-15, -7, -3) == -25

def test_multiple_positive_and_negative_numbers():
    assert sum(-15, 7, 3) == -5
    assert sum(10, -5, 2, -11, 10) == 6