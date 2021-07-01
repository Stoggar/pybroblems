import unittest
import find_duplicate


class TestDetectDuplicate(unittest.TestCase):
    def test_typical(self):
        data = [2, 4, 5, 3, 1, 2]
        expected = 2
        actual = find_duplicate.find_duplicate(data)
        assert actual == expected, f'expected {expected} got {actual}'

    def test_short(self):
        data = [1, 1]
        expected = 1
        actual = find_duplicate.find_duplicate(data)
        assert actual == expected, f'expected {expected} got {actual}'

    def test_beginning(self):
        data = [3, 3, 2, 1, 4, 5, 6]
        expected = 3
        actual = find_duplicate.find_duplicate(data)
        assert actual == expected, f'expected {expected} got {actual}'

    def test_end(self):
        data = [2, 1, 4, 5, 6, 3, 3]
        expected = 3
        actual = find_duplicate.find_duplicate(data)
        assert actual == expected, f'expected {expected} got {actual}'


if __name__ == '__main__':
    unittest.main()
    
