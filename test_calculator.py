from calculator import calculate_discount

def test_discount():
    assert calculate_discount(200, 10) == 180
