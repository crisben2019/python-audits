from src.sum import sum

def test_2_positive_numbers():
    assert sum(2, 3) == 5
    assert sum(5, 4) == 9
    assert sum(10, 5) == 15

def test_2_negative_numbers():
    assert sum(-2, -3) == -5
    assert sum(-5, -4) == -9
    assert sum(-10, -5) == -15

def test_2_positive_and_negative_numbers():
    assert sum(2, -3) == -1
    assert sum(5, -4) == 1
    assert sum(-10, 5) == -5