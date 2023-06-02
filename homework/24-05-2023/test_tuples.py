"""
this is an example of usage pytest library
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
from tuples import tuple_to_int2


def test_returns_number():
    res = tuple_to_int2((1, 2))
    print('tuple_to_int2 result must be an int type')
    assert type(res) == int


def test_build_proper_number_from_tuple():
    res = tuple_to_int2((1, 2,))
    assert res == 12


def test_raising_error_on_non_tuple():
    with pytest.raises(TypeError) as error:
        res = tuple_to_int2(999)
    assert 'object is not reversible' in str(error.value)
    # TODO: обсудить почему это плохой тест
