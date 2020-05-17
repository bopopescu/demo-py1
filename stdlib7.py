import unittest

def average(values):
    return sum(values,0.0)/len(values)

def add(values):
    return sum(values,0.0)


print(average([4,5,6]))


class TestAverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20,30,70]),40.0)
        self.assertEqual(round(average([1,5,7]),1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20,30,70)

    def test_add(self):
        self.assertEqual(add([20, 30, 70]), 120.0)


unittest.main()