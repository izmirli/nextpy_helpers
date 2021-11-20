"""1.3 Unit + 1.4 Unit."""
import re
import pytest
from hashlib import md5
from typing import Sequence
from inspect import getsourcelines


# 1.3.1
def intersection(list_1: list, list_2: list) -> list:
    """Find uniqe numbers that exist in both given lists.

    >>> intersection([1, 2, 3, 4], [8, 3, 9])
    [3]

    :param list_1: 1st list of numbers
    :param list_2: 2nd list of numbers
    :return: list of intersecting numbers
    """
    pass


def test_intersection():
    """Test intersection."""
    func_code, _ = getsourcelines(intersection)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("intersection function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert intersection([1, 2, 3, 4], [8, 3, 9]) == [3]
    assert intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]) == [5, 6]


# 1.3.2
def is_prime(number: int) -> bool:
    """Check if given number is a prime number.

    >>> is_prime(42)
    False
    >>> is_prime(43)
    True

    :param number: the number to check
    :return: True if number is prime, False otherwise
    """
    pass


def test_is_prime():
    """Test test_is_prime."""
    func_code, _ = getsourcelines(is_prime)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("is_prime function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert is_prime(42) is False
    assert is_prime(43) is True


# 1.3.3
def is_funny(string: str) -> bool:
    """Check if given string is funny = string has just 'a' and 'h' characters.

    >>> is_funny("hahahahahaha")
    True

    :param string: the string to check
    :return: True if string is funny, False otherwise.
    """
    pass


def test_is_funny():
    """Test is_funny."""
    func_code, _ = getsourcelines(is_funny)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("is_funny function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert is_funny("hahahahahaha") is True
    assert is_funny("abc") is False


# 1.3.4
def decipher(text: str) -> str:
    """Decipher given text according to hint: k->m; o->q; e->g.

    >>> decipher('koe')
    'mqg'

    :param text: the text to decipher
    :return: the deciphered text
    """
    pass


def test_decipher():
    """Test decipher."""
    func_code, _ = getsourcelines(decipher)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("decipher function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    md5_result = md5(decipher(password).encode()).hexdigest()
    assert md5_result == '5aeb4bf6184f2f0682d02a86d01aa35c'


# 1.4
def combine_coins(coin: str, numbers: Sequence) -> str:
    """Produse a string that combine coin symbol with each given number.

    >>> combine_coins('$', [1, 2, 3])
    '$1, $2, $3'

    :param coin: the coin symbol
    :param numbers: a list of numbers
    :return: the combined string
    """
    pass


def test_combine_coins():
    """Test combine_coins."""
    func_code, _ = getsourcelines(combine_coins)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("combine_coins function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    combine_coins_res = combine_coins('$', list(range(5)))
    assert combine_coins_res == '$0, $1, $2, $3, $4'
    assert combine_coins('₪', [100, 2, 777, 19]) == '₪100, ₪2, ₪777, ₪19'


def count_inner_function_code_lines(code_lines: list) -> int:
    """Count inner code lines of function.

     excluding: definition, empty lines, and .

    :param code_lines: list of function's code lines
    :return: number of code lines.
    """
    inner_code_lines = 0
    docstring_mode = False
    for line in map(lambda s: s.strip(), code_lines):
        # empty, "pass" or comment line.
        if line == '' or line == 'pass' or line.startswith('#'):
            continue

        if re.search(r'^def ', line):  # definition
            continue

        if not docstring_mode and re.search(r'^"""', line):   # start docstring
            if not re.search(r'""".*"""$', line):  # not a single-line docstring
                docstring_mode = True

            continue

        if docstring_mode:
            if re.search(r'"""$', line):  # end of docstring
                docstring_mode = False

            continue

        inner_code_lines += 1

    return inner_code_lines


def main():
    print(f"1.3.1 intersection([1, 2, 3, 4], [8, 3, 9]): {intersection([1, 2, 3, 4], [8, 3, 9])}")
    print(f"1.3.2 is_prime(43): {is_prime(43)}")
    print(f"1.3.3 is_funny('hahahahahaha'): {is_funny('hahahahahaha')}")
    print(f"1.3.4 decipher('sljmai ugrf rfc ambc: lglc dmsp mlc rum'): "
          f"{decipher('sljmai ugrf rfc ambc: lglc dmsp mlc rum')}")
    print()
    print(f"{'1.4':5} combine_coins('$', range(5)): {combine_coins('$', range(5))}")


if __name__ == "__main__":
    main()
