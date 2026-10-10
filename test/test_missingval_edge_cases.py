"""Edge case tests for missingval parameter."""

from tabulate import tabulate


def test_missingval_as_list():
    """missingval can be a list of replacement values per column"""
    data = [["Alice", 10], ["Bob", None], [None, 30]]
    result = tabulate(data, missingval=["n/a", "?"], tablefmt="plain")
    assert "n/a" in result
    assert "?" in result


def test_missingval_as_tuple():
    """missingval can be a tuple of replacement values per column"""
    data = [[None, 10], ["Bob", None]]
    result = tabulate(data, missingval=("MISSING", "?"), tablefmt="plain")
    assert "MISSING" in result
    assert "?" in result


def test_missingval_list_shorter_than_columns():
    """missingval list shorter than column count uses default for remaining columns"""
    data = [["Alice", 10, "X"], ["Bob", None, None], [None, 30, None]]
    result = tabulate(data, missingval=["n/a"], tablefmt="plain")
    # First column uses "n/a", other columns use default ""
    assert "n/a" in result


def test_missingval_empty_list():
    """missingval as empty list uses default for all columns"""
    data = [["Alice", 10], ["Bob", None]]
    result = tabulate(data, missingval=[], tablefmt="plain")
    # None should be replaced with default ""
    lines = result.split('\n')
    assert len(lines) >= 2


def test_missingval_with_none_values():
    """missingval replaces None values in data"""
    data = [[None, None], [1, 2]]
    result = tabulate(data, missingval="NONE", tablefmt="plain")
    assert "NONE" in result
    assert result.count("NONE") == 2
