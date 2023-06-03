"""
this is an example of usage unittest library
https://docs.python.org/3/library/unittest.html
"""

import unittest
from tuples import tuple_to_int2


class TestTupleToInt(unittest.TestCase):
    def setUp(self) -> None:
        self.simple_tuple = (1, 2)

    def test_returns_number(self):
        res = tuple_to_int2(self.simple_tuple)
        self.assertTrue(type(res) == int, 'should return number')

    def test_build_proper_number_from_tuple(self):
        res = tuple_to_int2(self.simple_tuple)
        self.assertEqual(res, 12, '(1,2) should return "12"')

    # def test_works_with_higher_ranks(self):
    #     res = tuple_to_int2((12, 34))
    #     self.assertEqual(res, 1234, 'should handle ranks bigger than one')

    def test_raising_error_on_non_tuple(self):
        with self.assertRaises(TypeError):
            res = tuple_to_int2(999)
            self.assertEqual(res, 12, 'Should fall with error on not tuple input')


# полезно включать все корнер-кейсы, в том числе (но не только):
# - нулевые значения и очень большие значения,
# - вызов без аргументов (должны ли быть дефолтные значения)
# - вызов с пустыми аргументами типа пустого массива
