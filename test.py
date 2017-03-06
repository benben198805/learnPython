import unittest

def fact(n):
    if n == 0 or isinstance(n, int) == False:
        raise AttributeError("wrong input")
    if n == 1:
        return 1
    return n * fact(n-1)


class TestFact(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fact(1), 1)

    def test_5(self):
        self.assertEqual(fact(5), 120)

    def test_0(self):
        with self.assertRaises(AttributeError):
            fact(0)

    def test_a(self):
        with self.assertRaises(AttributeError):
            fact('a')

if __name__ == '__main__':
    unittest.main()