"""1.1 Unit."""
import re
import pytest
from inspect import getsourcelines
from collections.abc import Sequence


# ex0
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
        pytest.skip("function is not yet implemented.")

    combine_coins_res = combine_coins('$', list(range(5)))
    assert combine_coins_res == '$0, $1, $2, $3, $4'
    assert combine_coins('₪', [100, 2, 777, 19]) == '₪100, ₪2, ₪777, ₪19'


# 1.1.2
def double_letter(my_str: str) -> str:
    """Return a string where each character from given string is doubled.

    >>> double_letter("python")
    'ppyytthhoonn'

    :param my_str:
    :return: the new string
    """
    pass


def test_double_letter():
    """Test double_letter."""
    func_code, _ = getsourcelines(double_letter)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert double_letter("python") == 'ppyytthhoonn'
    assert double_letter("we are the champions!") == 'wwee  aarree  tthhee  cchhaammppiioonnss!!'


# 1.1.3
def four_dividers(number: int) -> list:
    """Find all number, up to given one, that divide by 4 without remainder.

    >>> four_dividers(9)
    [4, 8]
    >>> four_dividers(3)
    []

    :param number: top limit
    :return: list of numbers divide by 4 without remainder
    """
    pass


def test_four_dividers():
    """Test four_dividers."""
    func_code, _ = getsourcelines(four_dividers)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert four_dividers(9) == [4, 8]
    assert four_dividers(3) == []


# 1.1.4
def sum_of_digits(number: int) -> int:
    """Sum each digit in given number.

    >>> sum_of_digits(104)
    5

    :param number: the number to supup its digits
    :return: the sum of all digits
    """
    pass


def test_sum_of_digits():
    """Test sum_of_digits."""
    func_code, _ = getsourcelines(sum_of_digits)
    inner_lines_count = count_inner_function_code_lines(func_code)
    if inner_lines_count == 0:
        pytest.skip("function is not yet implemented.")
    assert inner_lines_count <= 1, "Function code block should have only 1 line"

    assert sum_of_digits(104) == 5


def count_inner_function_code_lines(code_lines: list) -> int:
    """Count inner code lines of function.

     excluding: definition, empty lines, and .

    :param code_lines: list of function's code lines
    :return: number of code lines.
    """
    inner_code_lines = 0
    inner_code_text = ''
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
    print(f"{'0':5} combine_coins('$', range(5)): {combine_coins('$', range(5))}")
    print()
    print(f"1.1.2 double_letter('python'): {double_letter('python')}")
    print(f"1.1.3 four_dividers(9): {four_dividers(9)}")
    print(f"1.1.4 sum_of_digits(104): {sum_of_digits(104)}")


if __name__ == "__main__":
    main()
