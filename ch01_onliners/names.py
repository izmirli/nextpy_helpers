"""Unit 1.5 - concluding exercise."""
import re
from inspect import getsourcelines
from functools import partial

NAMES_FILE = 'names.txt'
NAMES_LENGTH_FILE = 'names_length.txt'


# 1.5.1 (up to 2 lines of code)
def print_longest_name():
    """Find and print longest name from given list.

    :return: None
    """
    pass


# 1.5.2 (up to 2 lines of code)
def print_sum_of_names_length():
    """Sum and print the length of all given names.

    :return: None
    """
    pass


# 1.5.3 (up to 4 lines of code)
def print_shortest_names():
    """Fined and print shortest names in given list (each name in separate line).

    :return: None
    """
    pass


# 1.5.4 (up to 3 lines of code)
def create_file_with_names_length():
    """Fined names length and save them in new file.

    :return: None
    """
    pass


# 1.5.5 (up to 3 lines of code)
def print_names_by_length():
    """Get length from user and print names with this length.

    :return: None
    """
    pass


def main():
    print_longest_name()
    print_sum_of_names_length()
    print_shortest_names()
    create_file_with_names_length()
    print_names_by_length()


# tests for functions - use with pytest
def test_print_longest_name(capsys):
    """Test print_longest_name."""
    print_longest_name()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Vladimir'

    func_code, _ = getsourcelines(print_longest_name)
    assert count_inner_function_code_lines(func_code) <= 2


def test_print_sum_of_names_length(capsys):
    """Test print_sum_of_names_length."""
    print_sum_of_names_length()
    captured = capsys.readouterr()
    assert captured.out.strip() == '38'

    func_code, _ = getsourcelines(print_sum_of_names_length)
    assert count_inner_function_code_lines(func_code) <= 2


def test_print_shortest_names(capsys):
    """Test print_shortest_names."""
    print_shortest_names()
    captured = capsys.readouterr().out.strip()
    assert captured == 'Ed\nJo' or captured == 'Jo\nEd'

    func_code, _ = getsourcelines(print_shortest_names)
    assert count_inner_function_code_lines(func_code) <= 4


def test_create_file_with_names_length(monkeypatch, tmpdir):
    """Test create_file_with_names_length."""
    read_names_open = partial(open, NAMES_FILE, 'r')
    tmp_names_length = tmpdir.join(NAMES_LENGTH_FILE)
    write_names_length_open = partial(open, tmp_names_length, 'w')

    def mock_open(path: str, mode: str):
        """Mock open for calls done by create_file_with_names_length."""
        if path == NAMES_FILE and mode == 'r':
            return read_names_open()
        elif path == NAMES_LENGTH_FILE and mode == 'w':
            return write_names_length_open()
        else:
            raise RuntimeError(f'Unexpected open parameters ({path}, {mode})')

    monkeypatch.setattr('builtins.open', mock_open)
    create_file_with_names_length()
    monkeypatch.undo()
    content = tmp_names_length.read()
    assert content == '4\n4\n8\n7\n2\n5\n6\n2\n'

    func_code, _ = getsourcelines(create_file_with_names_length)
    assert count_inner_function_code_lines(func_code) <= 3


def test_print_names_by_length(capsys, monkeypatch):
    """Test print_names_by_length."""
    monkeypatch.setattr('builtins.input', lambda _: '4')
    print_names_by_length()
    captured = capsys.readouterr().out.strip()
    assert captured == 'Hans\nAnna' or captured == 'Anna\nHans'

    func_code, _ = getsourcelines(print_names_by_length)
    assert count_inner_function_code_lines(func_code) <= 3


def count_inner_function_code_lines(code_lines: list) -> int:
    """Count inner code lines of function.

     excluding: definition, empty lines, and .

    :param code_lines: list of function's code lines
    :return: number of code lines.
    """
    inner_code_lines = 0
    docstring_mode = False
    for line in map(lambda s: s.strip(), code_lines):
        if line == '' or line.startswith('#'):  # empty or comment line.
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


if __name__ == '__main__':
    main()
